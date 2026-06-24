from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] += (nums[nums[i] % n] % n) * n
        return [num // n for num in nums]


if __name__ == "__main__":
    solution = Solution()

    assert solution.buildArray([0, 2, 1, 5, 3, 4]) == [0, 1, 2, 4, 5, 3]
    assert solution.buildArray([5, 0, 1, 2, 3, 4]) == [4, 5, 0, 1, 2, 3]
    print("All test cases passed!")
