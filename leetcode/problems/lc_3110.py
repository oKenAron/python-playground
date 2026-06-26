class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1))


if __name__ == "__main__":
    solution = Solution()

    assert solution.scoreOfString("hello") == 13
    assert solution.scoreOfString("zaz") == 50
    print("All test cases passed!")
