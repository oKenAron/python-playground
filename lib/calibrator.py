#!/usr/bin/env python3
"""
环境复杂度标定器 (Environment Complexity Calibrator)
============================================================
Developed with assistance from Claude (Anthropic).

目的：用一组复杂度已知且干净的"标尺"函数，在真实运行环境里反复测量，
      反推出这台机器的：
        1. 噪声基线（同一规模多次运行的波动幅度）
        2. 每种复杂度的实测拟合指数（理论值 vs 实测值的偏差）
      以后测未知程序时，拿它的实测指数去对照这套标尺即可。

设计原则：
  - 标尺函数全部用纯CPU计算，无IO、无subprocess、无递归（避开深度限制和进程启动噪声）
  - 每个规模重复多次取最小值（最小值最接近真实算法耗时，干扰只会让耗时变长）
  - 用 log-log 线性回归拟合复杂度指数：若 T = c * n^k，则 log T = log c + k * log n，
    斜率 k 就是实测复杂度指数
  - 多规模跨度足够大，让真实计算耗时远超噪声

规模选择经验法则（重要）：
  每个测量点的耗时最好落在【几十ms ~ 一两秒】这个窗口：
    - 下限：耗时要明显高于噪声基线（几十ms以上），否则被随机抖动污染，拟合不准
    - 上限：单次别超过1-2秒，否则长时间运行容易被CPU降频/系统调度打断
      （尤其笔记本有功耗墙时，长任务后半段降速会把指数人为拉高）
  如果某档拟合指数偏离理论值较多，先检查是不是某些点耗时太小或太大。
"""

import math
import time

# ============================================================
# 可调参数（集中在此，按机器情况调整）
# ============================================================
REPEATS = 5  # 每个规模点重复测量次数，取最小值。噪声大的机器可调高到15~20
WARMUP_SECONDS = 3.0  # 正式测量前的预热时长（秒）
NOISE_REPEATS = 100  # 噪声基线测量的重复次数
SAFE_MS = 20.0  # 单点耗时低于此值(毫秒)视为可能受噪声影响，会被标记


# ============================================================
# 标尺函数：复杂度明确、实现干净
# ============================================================


def ruler_O1(n):
    """O(1) - 与n无关的固定工作量（加大到耗时可测量的量级）"""
    x = 0
    for _ in range(2000000):
        x += 1
    return x


def ruler_On(n):
    """O(n) - 单层线性循环"""
    x = 0
    for i in range(n):
        x += i
    return x


def ruler_Onlogn(n):
    """O(n log n) - 排序是最干净的代表"""
    data = [(i * 2654435761) % n for i in range(n)]  # 伪随机但确定性的数据
    data.sort()
    return data[0]


def ruler_On2(n):
    """O(n^2) - 双层嵌套循环"""
    x = 0
    for i in range(n):
        for j in range(n):
            x += 1
    return x


def ruler_On3(n):
    """O(n^3) - 三层嵌套循环"""
    x = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                x += 1
    return x


# ============================================================
# 计时核心
# ============================================================


def time_func(func, n, repeats=REPEATS):
    """对 func(n) 运行 repeats 次，返回最小耗时（最接近真实算法耗时）"""
    best = float("inf")
    for _ in range(repeats):
        start = time.perf_counter()
        func(n)
        elapsed = time.perf_counter() - start
        if elapsed < best:
            best = elapsed
    return best


def fit_exponent(sizes, times):
    """
    用 log-log 最小二乘回归拟合复杂度指数 k（假设 T = c * n^k）。
    只用耗时足够大（脱离噪声）的点参与拟合。
    返回 (拟合指数k, 参与拟合的点数)。
    """
    # 过滤掉耗时太小的点（容易被噪声主导）
    pts = [(s, t) for s, t in zip(sizes, times) if t > 1e-5]
    if len(pts) < 2:
        return None, len(pts)
    xs = [math.log(s) for s, t in pts]
    ys = [math.log(t) for s, t in pts]
    n = len(xs)
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    num = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    den = sum((x - mean_x) ** 2 for x in xs)
    if den == 0:
        return None, n
    k = num / den
    return k, n


def warmup(seconds=3.0):
    """正式测量前空跑若干秒，把CPU频率从节能态拉到稳态、预热缓存。
    对有功耗墙/频率调度敏感的笔记本(如T480)尤其重要：
    冷启动时前几次测量会偏慢，预热后结果更稳定。"""
    print(f"预热中（{seconds}秒，拉升CPU频率到稳态）...", end="", flush=True)
    end_time = time.perf_counter() + seconds
    x = 0
    while time.perf_counter() < end_time:
        for i in range(100000):
            x += i
    print(" 完成")
    return x


def measure_noise(func, n, repeats):
    """同一规模跑很多次，统计波动幅度（噪声基线）。
    用分位数而非max-min，避免极少数被系统调度打断的离群点造成误导。"""
    samples = []
    for _ in range(repeats):
        start = time.perf_counter()
        func(n)
        samples.append(time.perf_counter() - start)
    samples.sort()
    mn = samples[0]
    med = samples[len(samples) // 2]
    p90 = samples[int(len(samples) * 0.9)]
    mx = samples[-1]
    # 稳健抖动：最小值到90分位（剔除离群点后的典型波动）
    robust_jitter = (p90 - mn) / med if med > 0 else 0
    return mn, med, p90, mx, robust_jitter


# ============================================================
# 主流程
# ============================================================


def main():
    print("=" * 60)
    print("环境复杂度标定器")
    print("=" * 60)
    print()

    # ---------- 第零部分：预热 ----------
    warmup(WARMUP_SECONDS)

    # ---------- 第一部分：噪声基线测量 ----------
    print(f"\n【1】噪声基线测量（同一规模重复{NOISE_REPEATS}次，看波动）")
    print("-" * 60)
    mn, med, p90, mx, jitter = measure_noise(ruler_On, 100000, repeats=NOISE_REPEATS)
    print(f"O(n)@n=100000 重复{NOISE_REPEATS}次:")
    print(f"  最小={mn * 1000:.3f}ms  中位={med * 1000:.3f}ms  90分位={p90 * 1000:.3f}ms  最大={mx * 1000:.3f}ms")
    print(f"  稳健抖动 (p90-min)/median = {jitter * 100:.1f}%  (剔除离群点的典型波动)")
    print(f"  注: 最大值{mx * 1000:.1f}ms是被系统调度偶发打断的离群点,取最小值即可规避")

    # ---------- 第二部分：各标尺复杂度拟合 ----------
    print("\n【2】标尺复杂度拟合（log-log回归，理论值 vs 实测值）")
    print("-" * 60)

    rulers = [
        ("O(1)", ruler_O1, 0.0, [1000000, 2000000, 4000000, 8000000, 16000000]),
        ("O(n)", ruler_On, 1.0, [400000, 800000, 1600000, 3200000, 6400000]),
        ("O(n log n)", ruler_Onlogn, 1.0, [100000, 200000, 400000, 800000, 1600000]),  # 理论k略大于1
        ("O(n^2)", ruler_On2, 2.0, [600, 1200, 2400, 4800]),
        ("O(n^3)", ruler_On3, 3.0, [120, 160, 220, 300]),
    ]

    results = []
    for name, func, theory_k, sizes in rulers:
        times = [time_func(func, n) for n in sizes]
        k, npts = fit_exponent(sizes, times)
        # 记录一个中间规模点作为"速度基准"（避开首尾，取中间最有代表性）
        mid_idx = len(sizes) // 2
        bench_n, bench_t = sizes[mid_idx], times[mid_idx]
        results.append((name, theory_k, k, bench_n, bench_t))
        print(f"\n{name}  (理论指数={theory_k})")
        for s, t in zip(sizes, times):
            flag = "" if t * 1000 >= SAFE_MS else "  <- 耗时偏小,易受噪声影响"
            print(f"    n={s:>8d}  耗时={t * 1000:>10.3f}ms{flag}")
        if k is not None:
            note = ""
            if name == "O(n log n)":
                note = "  (logn项会让实测略高于1，正常)"
            print(f"    => 实测拟合指数 k = {k:.3f}{note}")
        else:
            print("    => 耗时太小无法可靠拟合")

    # ---------- 第三部分：总结表 ----------
    print("\n" + "=" * 60)
    print("【3】标定结果汇总")
    print("=" * 60)
    print(f"{'复杂度':12s} {'理论指数':>8s} {'实测指数':>8s} {'指数偏差':>8s}")
    print("-" * 42)
    exp_biases = []
    for name, theory_k, k, bn, bt in results:
        if k is not None:
            diff = k - theory_k
            # O(n log n) 的偏差含 logn 项的真实贡献，不是纯环境噪声，排除出平均
            if name != "O(n log n)":
                exp_biases.append(diff)
            print(f"{name:12s} {theory_k:>8.2f} {k:>8.3f} {diff:>+8.3f}")
        else:
            print(f"{name:12s} {theory_k:>8.2f} {'N/A':>8s} {'--':>8s}")

    # ---------- 第四部分：环境BIAS报告（核心输出）----------
    print("\n" + "=" * 60)
    print("【4】环境 BIAS 报告（这才是可带走、可复用的校准结果）")
    print("=" * 60)

    # bias-1: 指数系统性偏移（已排除O(n log n)，仅取纯幂律档位）
    avg_exp_bias = sum(exp_biases) / len(exp_biases) if exp_biases else 0
    print(f"\n[BIAS-1] 指数系统性偏移 = {avg_exp_bias:+.3f}  (取纯幂律档位O(1)/O(n)/O(n^2)/O(n^3)的平均)")
    print(f"  含义: 本机+本方法测出的复杂度指数, 平均比理论值偏高 {avg_exp_bias:+.3f}")
    print(f"  用法: 测未知程序得到指数X时, 真实复杂度更接近 X - ({avg_exp_bias:+.3f})")
    print(f"        例如测出2.05, 减去偏移后约{2.05 - avg_exp_bias:.2f}, 判定为O(n^2)")

    # bias-2: 绝对速度基准（用O(n)那一档作为单位速度参照）
    on_bench = next((r for r in results if r[0] == "O(n)"), None)
    if on_bench:
        _, _, _, bn, bt = on_bench
        ns_per_op = (bt / bn) * 1e9  # 每次基本操作耗时(纳秒)
        print("\n[BIAS-2] 绝对速度基准 (单位运算耗时)")
        print(f"  O(n)档 n={bn} 耗时={bt * 1000:.2f}ms")
        print(f"  => 每次基本循环操作约 {ns_per_op:.1f} 纳秒")
        print(f"  用法: 估算某算法在规模N下的耗时 ≈ (操作总数) × {ns_per_op:.1f}ns")
        print("        据此判断会不会超过评测平台的时限")

    # bias-3: 噪声水平
    print(f"\n[BIAS-3] 噪声水平 = 稳健抖动约 {jitter * 100:.1f}%")
    print("  含义: 同一程序重复测量, 典型波动在此范围内")
    print("  用法: 两次测量差异小于此值时, 视为无显著区别(不要过度解读)")

    print("\n建议: 把以上3个BIAS连同机器型号记下来存档, 换机器或隔段时间重跑对比。")


if __name__ == "__main__":
    main()
