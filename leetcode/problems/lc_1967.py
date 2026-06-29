from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        for pattern in patterns:
            if word.find(pattern) != -1:
                ans += 1
        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.numOfStrings(["a", "abc", "bc", "d"], "abc") == 3
    assert solution.numOfStrings(["a", "b", "c"], "aaaaabbbbb") == 2
    assert solution.numOfStrings(["a", "a", "a"], "ab") == 3
    print("All test cases passed!")
