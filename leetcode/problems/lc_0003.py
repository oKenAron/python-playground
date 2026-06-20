class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen: dict[str, int] = {}
        left, ans = 0, 0
        for i in range(len(s)):
            # seen[char] 可能是窗口外的旧位置(已经被 left 跳过),
            # 必须确认它落在当前窗口内(>= left)才能用来更新 left,否则 left 会被错误地往回拉
            # assert new_left >= left, f"left 不应该后退: {left} -> {new_left}"
            if s[i] in seen and seen[s[i]] >= left:
                left = seen[s[i]] + 1
            seen[s[i]] = i
            ans = max(ans, i - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()

    test_case_A = solution.lengthOfLongestSubstring("abcabcbb")
    test_case_B = solution.lengthOfLongestSubstring("bbbbb")
    test_case_C = solution.lengthOfLongestSubstring("pwwkew")
    test_case_addition = solution.lengthOfLongestSubstring("abba")
    assert test_case_A == 3, test_case_A
    assert test_case_B == 1, test_case_B
    assert test_case_C == 3, test_case_C
    assert test_case_addition == 2, test_case_addition
    print("All test cases passed!")
