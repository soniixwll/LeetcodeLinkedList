# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        first_fake_node = ListNode()

        tail = first_fake_node
        probe = head
        first_fake_node.next = probe

        while probe and probe.next:

            first = probe
            second = probe.next
            third = second.next

            second.next = first
            first.next = third

            tail.next = second
            # tail = second

            probe = third
            tail = first


        return first_fake_node.next
