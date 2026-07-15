from collections import deque


class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        # 访问 string[i] 是个on操作吗？惊了
        deq_s = deque(s)
        deq_t = deque(t)
        diff_length = len(t) - len(s)
        if diff_length < 0:
            return False
        while deq_s:
            if diff_length < -1:
                return False
            while deq_s.popleft() != deq_t.popleft():
                while diff_length < 0:
                    return False
                if not deq_s:
                    diff_length -= 1
                    break
                temp_deq_s = deq_s.copy()
                temp_deq_t = deq_t.copy()
                temp_diff_length = diff_length
                while temp_deq_s.popleft() != temp_deq_t.popleft():
                    if temp_diff_length < 0:
                        break
                    temp_diff_length -= 1
                    if not temp_deq_s:
                        return True
                if diff_length > 0 and not temp_deq_s:
                    return True
                diff_length -= 1
        return True


if __name__ == "__main__":
    solution = Solution()

    result_a = solution.canMakeSubsequence("cat", "chat")
    result_b = solution.canMakeSubsequence("plane", "apple")
    result_c = solution.canMakeSubsequence("aa", "bbbb")
    result_extreme = solution.canMakeSubsequence(
        "abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdea",
        "abcdeabcdeabcdexxxxxabcdeabcdeaxbcdeabcdeabcdexxxxxabcdeabcdeabxxxxxcdeabcdeabxxxxxcdeabcdea",
    )

    assert result_a, f"Error In Test Case A: {result_a}"
    assert not result_b, f"Error In Test Case B: {result_b}"
    assert not result_c, f"Error In Test Case C: {result_c}"
    assert result_extreme, f"Error In Test Case E: {result_extreme}"

    print("All test cases passed!")
