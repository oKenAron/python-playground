class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, max = 0, 0
        if len(s) == 1:
            return 1
        for right in range(1, len(s)):
            while left < right and s[right] in s[left:right]:
                left += 1
            if right - left + 1 > max:
                max = right - left + 1
        return max


if __name__ == "__main__":
    solution = Solution()

    test_case_A = solution.lengthOfLongestSubstring("abcabcbb")
    test_case_B = solution.lengthOfLongestSubstring("bbbbb")
    test_case_C = solution.lengthOfLongestSubstring("pwwkew")
    assert test_case_A == 3, test_case_A
    assert test_case_B == 1, test_case_B
    assert test_case_C == 3, test_case_C
    print("All test cases passed!")
