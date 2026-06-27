from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(1 for num in nums if num % 3 != 0)


if __name__ == "__main__":
    solution = Solution()

    assert solution.minimumOperations([1, 2, 3, 4]) == 3
    assert solution.minimumOperations([3, 6, 9]) == 0
    print("All test cases passed!")
