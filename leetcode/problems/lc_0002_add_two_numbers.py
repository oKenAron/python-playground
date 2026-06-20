# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from unittest import result

from lc_utils import ListNode, build_linked_list, linked_list_to_list


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ans = ListNode()
        ans_sign = ans
        while True:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            add_before_carry = n1 + n2 + ans_sign.val
            ans_sign.val = (
                add_before_carry if add_before_carry < 10 else add_before_carry - 10
            )
            if not l1 and not l2 and add_before_carry >= 10:
                ans_sign.next = ListNode(1)
                return ans
            elif not l1 and not l2:
                return ans
            ans_sign.next = ListNode() if add_before_carry < 10 else ListNode(1)
            ans_sign = ans_sign.next


if __name__ == "__main__":
    solution = Solution()

    result_A = linked_list_to_list(
        solution.addTwoNumbers(
            build_linked_list([2, 4, 3]), build_linked_list([5, 6, 4])
        )
    )
    assert result_A == [7, 0, 8], result_A
    result_B = linked_list_to_list(
        solution.addTwoNumbers(
            build_linked_list([0]), build_linked_list([0]])
        )
    )
    assert result_B == [0], result_B
    result_C = linked_list_to_list(
        solution.addTwoNumbers(
            build_linked_list([9,9,9,9,9,9,9]), build_linked_list([9,9,9,9])
        )
    )
    assert result_C == [8,9,9,9,0,0,0,1], result_C
