class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        length = len(nums)
        ans = 0
        for i in range(length):
            for j in range(i, length):
                sum_subarray = sum(nums[i : j + 1])
                if sum_subarray % 10 == x and str(sum_subarray)[0] == str(x):
                    ans += 1

        return ans
