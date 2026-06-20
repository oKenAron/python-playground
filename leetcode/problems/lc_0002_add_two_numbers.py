# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from lc_utils import ListNode, build_linked_list, linked_list_to_list


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        pointer = dummy
        carry = 0
        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            added = n1 + n2 + carry
            # divmod(a, b) 一次性返回 (a // b, a % b)
            # 例: divmod(13, 10) == (1, 3)
            # 处理进位时可以写成: carry, digit = divmod(total, 10)
            carry = added // 10
            pointer.next = ListNode(added % 10)
            pointer = pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


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
