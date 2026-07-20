class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        return (start[0] - target[0] + start[1] - target[1]) % 2 == 0
