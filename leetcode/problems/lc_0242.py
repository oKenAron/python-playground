from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    solution = Solution()

    result_a = solution.isAnagram("anagram", "nagaram")
    result_b = solution.isAnagram("rat", "car")

    assert result_a, f"Error In Test Case A: {result_a}"
    assert not result_b, f"Error In Test Case B: {result_b}"

    print("All test cases passed!")
