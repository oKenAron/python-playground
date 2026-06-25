class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t


if __name__ == "__main__":
    solution = Solution()

    assert solution.theMaximumAchievableX(4, 1) == 6
    assert solution.theMaximumAchievableX(3, 2) == 7
    print("All test cases passed!")
