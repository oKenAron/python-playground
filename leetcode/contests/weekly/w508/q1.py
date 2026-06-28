import copy


class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        t = copy.deepcopy(nums)

        ans = 0
        for _ in range(k):
            number = max(t)
            index = t.index(number)
            t[index] = 0
            ans += number * mul
            if mul > 1:
                mul -= 1
        return ans


sol = Solution()
print(sol.maxSum([6, 1, 2, 9], 3, 2))
print(sol.maxSum([3, 7, 5, 2], 2, 4))
