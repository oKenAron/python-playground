import heapq


class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        max_nums = heapq.nlargest(k, nums)
        ans = 0

        for num in max_nums:
            ans += num * mul
            if mul > 1:
                mul -= 1

        return ans


sol = Solution()
print(sol.maxSum([6, 1, 2, 9], 3, 2))
print(sol.maxSum([3, 7, 5, 2], 2, 4))
