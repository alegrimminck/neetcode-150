from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        first = second = dummy

        while n >= 0:
            second = second.next
            n -= 1

        while second:
            first = first.next
            second = second.next

        first.next = first.next.next
        return dummy.next
