from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for o in operations:
            if o[1] == "+":
                ans += 1
            else:
                ans -= 1

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.finalValueAfterOperations(["--X", "X++", "X++"]) == 1
