from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        nums_or = 0
        ans = 0
        weight = 0
        for i in nums:
            nums_or |= i
        while nums_or != 0:
            ans += nums_or % 2 * 2 ** (len(nums) - 1) * 2**weight
            nums_or //= 2
            weight += 1

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_caseA = solution.subsetXORSum([1, 3])
    test_caseB = solution.subsetXORSum([5, 1, 6])
    test_caseC = solution.subsetXORSum([3, 4, 5, 6, 7, 8])
    assert test_caseA == 6, test_caseA
    assert test_caseB == 28, test_caseB
    assert test_caseC == 480, test_caseC
    print("All test cases passed!")
