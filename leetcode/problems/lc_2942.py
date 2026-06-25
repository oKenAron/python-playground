from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i in range(len(words)):
            if x in words[i]:
                ans.append(i)
        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.findWordsContaining(["leet", "code"], "e") == [0, 1]
    assert solution.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "a") == [0, 2]
    assert solution.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "z") == []
    print("All test cases passed!")
