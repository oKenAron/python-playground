from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(pattern in word for pattern in patterns)


if __name__ == "__main__":
    solution = Solution()

    assert solution.numOfStrings(["a", "abc", "bc", "d"], "abc") == 3
    assert solution.numOfStrings(["a", "b", "c"], "aaaaabbbbb") == 2
    assert solution.numOfStrings(["a", "a", "a"], "ab") == 3
    print("All test cases passed!")
