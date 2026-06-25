class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1_plus_num2 = (1 + n) * n // 2
        num2 = (1 + n // m) * m * (n // m) // 2

        return num1_plus_num2 - num2 * 2


if __name__ == "__main__":
    solution = Solution()

    assert solution.differenceOfSums(10, 3) == 19
    assert solution.differenceOfSums(5, 6) == 15
    assert solution.differenceOfSums(5, 1) == -15, solution.differenceOfSums(5, 1)
    print("All test cases passed!")
