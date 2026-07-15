class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        max_digit_range = 0
        ans = 0
        for num in nums:
            arr_num = list(str(num))
            if int(max(arr_num)) - int(min(arr_num)) > max_digit_range:
                ans = 0
                max_digit_range = int(max(arr_num)) - int(min(arr_num))
                ans += num
            elif int(max(arr_num)) - int(min(arr_num)) == max_digit_range:
                ans += num

        return ans


if __name__ == "__main__":
    solution = Solution()

    result_a = solution.maxDigitRange([5724, 111, 350])
    result_b = solution.maxDigitRange([90, 900])

    assert result_a == 6074, f"Error In Test Case A: {result_a}"
    assert result_b == 990, f"Error In Test Case B: {result_b}"

    print("All test cases passed!")
