from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums.append(nums[i])
        return nums


if __name__ == "__main__":
    solution = Solution()

    test_caseA = solution.getConcatenation([1, 2, 1])
    test_caseB = solution.getConcatenation([1, 3, 2, 1])

    assert test_caseA == [1, 2, 1, 1, 2, 1]
    assert test_caseB == [1, 3, 2, 1, 1, 3, 2, 1]
    print("All test cases passed!")
