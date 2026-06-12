# -----------------------------------------------------------------------
# Language : Python 3
# Editor   : Zed  （vim キーバインドのために採用）
# Platform : Paiza
#
# [方針]
#   - vibe coding・自動補全は使用しない
#   - 補助ツールに頼らず、すべて手で書く
# -----------------------------------------------------------------------
import sys


def solve():
    ans = 0

    # ロジック

    return ans


def main():
    raw = sys.stdin.read().split()
    if not raw:
        return

    tokens = iter(raw)

    def next_str():
        return next(tokens)

    def next_int():
        return int(next(tokens))

    # 入力データの受け取り

    # 計算実行と結果出力
    ans = solve()
    print(ans)


if __name__ == "__main__":
    main()
