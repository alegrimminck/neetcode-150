from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = slow = fast = ListNode()
        slow.next = fast.next = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev, slow.next = None, None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = dummy.next, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
