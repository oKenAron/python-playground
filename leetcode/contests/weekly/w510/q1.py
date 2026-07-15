class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        sta_H = int(startTime[0:2])
        sta_M = int(startTime[3:5])
        sta_S = int(startTime[6:8])
        end_H = int(endTime[0:2])
        end_M = int(endTime[3:5])
        end_S = int(endTime[6:8])
        diff_S = (end_S - sta_S) % 60
        if end_S >= sta_S:
            diff_M = (end_M - sta_M) % 60
        else:
            diff_M = (end_M - sta_M - 1) % 60
        if end_M > sta_M:
            diff_H = (end_H - sta_H) % 24
        elif end_M == sta_M and end_S < sta_S:
            diff_H = (end_H - sta_H - 1) % 24
        elif end_M == sta_M:
            diff_H = (end_H - sta_H) % 24
        else:
            diff_H = (end_H - sta_H - 1) % 24
        return diff_S + 60 * diff_M + 3600 * diff_H


if __name__ == "__main__":
    solution = Solution()

    result_a = solution.secondsBetweenTimes("01:00:00", "01:00:25")
    result_b = solution.secondsBetweenTimes("12:34:56", "13:00:00")
    result_c = solution.secondsBetweenTimes("01:00:30", "03:00:29")
    result_d = solution.secondsBetweenTimes("23:10:30", "01:12:29")

    assert result_a == 25, f"Error In Test Case A: {result_a}"
    assert result_b == 1504, f"Error In Test Case B: {result_b}"
    assert result_c == 7199, f"Error In Test Case C: {result_c}"
    assert result_d == 7319, f"Error In Test Case D: {result_d}"

    print("All test cases passed!")
