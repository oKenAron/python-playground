# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from lc_utils import ListNode, build_linked_list, linked_list_to_list


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        ans_sign = ans
        carry = 0
        sign = 1
        while sign:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            added = n1 + n2 + carry
            ans_sign.val = added % 10
            carry = added // 10
            sign = bool(l1 or l2 or carry)
            if sign:
                ans_sign.next = ListNode()
                ans_sign = ans_sign.next
        return ans


if __name__ == "__main__":
    solution = Solution()

    result_A = linked_list_to_list(solution.addTwoNumbers(build_linked_list([2, 4, 3]), build_linked_list([5, 6, 4])))
    assert result_A == [7, 0, 8], result_A

    result_B = linked_list_to_list(solution.addTwoNumbers(build_linked_list([0]), build_linked_list([0])))
    assert result_B == [0], result_B

    result_C = linked_list_to_list(
        solution.addTwoNumbers(build_linked_list([9, 9, 9, 9, 9, 9, 9]), build_linked_list([9, 9, 9, 9]))
    )
    assert result_C == [8, 9, 9, 9, 0, 0, 0, 1], result_C
