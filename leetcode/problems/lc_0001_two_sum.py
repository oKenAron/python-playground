class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 创建字典，键为value，值为index
        seen: dict[int, int] = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [i, seen[target - nums[i]]]
            elif nums[i] not in seen:
                seen[nums[i]] = i
        raise ValueError("Error")


if __name__ == "__main__":
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) in ([0, 1], [1, 0])
    assert solution.twoSum([3, 2, 4], 6) in ([1, 2], [2, 1])
    assert solution.twoSum([3, 3], 6) in ([0, 1], [1, 0])
    print("All test cases passed!")
