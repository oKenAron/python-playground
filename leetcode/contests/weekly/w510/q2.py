class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        total = sum(nums)
        incr_times = (total - 1) // k
        return incr_times * (1 + incr_times) // 2
