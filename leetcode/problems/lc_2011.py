from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if o[1] == "+" else -1 for o in operations)


if __name__ == "__main__":
    solution = Solution()

    assert solution.finalValueAfterOperations(["--X", "X++", "X++"]) == 1
