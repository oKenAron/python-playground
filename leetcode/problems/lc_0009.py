class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()

    assert solution.isPalindrome(121)
    assert not solution.isPalindrome(-121)
    assert not solution.isPalindrome(10)
    print("All test cases passed!")
