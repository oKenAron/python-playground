from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k


if __name__ == "__main__":
    solution = Solution()

    result_a = solution.minOperations([3, 9, 7], 5)
    result_b = solution.minOperations([4, 1, 3], 4)
    result_c = solution.minOperations([3, 2], 6)

    assert result_a == 4, f"Error In Test Case A: {result_a}"
    assert result_b == 0, f"Error In Test Case B: {result_b}"
    assert result_c == 5, f"Error In Test Case C: {result_c}"

    print("All test cases passed!")
