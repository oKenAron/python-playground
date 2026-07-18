from typing import List
import math

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return math.gcd(max(nums),min(nums))

if __name__ == "__main__":
    solution = Solution()

    result_a =  solution.findGCD([2,3,6,9,10])
    result_b =  solution.findGCD([7,5,6,8,3])
    result_c =  solution.findGCD([3,3])

    assert result_a == 2 , f"Error In Test Case A: {result_a}"
    assert result_b == 1 , f"Error In Test Case B: {result_b}"
    assert result_c == 3 , f"Error In Test Case C: {result_c}"

    print("All test cases passed!")
