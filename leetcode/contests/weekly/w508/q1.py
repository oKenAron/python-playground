class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        selected = [0 for _ in range(k)]
        for num in nums:
            for i in range(k):
                if num > selected[i]:
                    selected.pop()
                    selected.insert(i, num)
                    break
        ans = 0
        for i in selected:
            ans += i * mul
            if mul >= 2:
                mul -= 1
        return ans


sol = Solution()
print(sol.maxSum([6, 1, 2, 9], 3, 2))
print(sol.maxSum([3, 7, 5, 2], 2, 4))
