from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[num] for num in nums]


if __name__ == "__main__":
    solution = Solution()

    assert solution.buildArray([0, 2, 1, 5, 3, 4]) == [0, 1, 2, 4, 5, 3]
    assert solution.buildArray([5, 0, 1, 2, 3, 4]) == [4, 5, 0, 1, 2, 3]
