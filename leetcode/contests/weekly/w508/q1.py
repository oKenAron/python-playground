class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        ans = 0
        while k:
            current_max = max(nums)
            if mul >= 1:
                ans += mul * current_max
                mul -= 1
            else:
                ans += current_max
            nums.pop(nums.index(current_max))
            k -= 1
        return ans


sol = Solution()
print(sol.maxSum([6, 1, 2, 9], 3, 2))
print(sol.maxSum([3, 7, 5, 2], 2, 4))
