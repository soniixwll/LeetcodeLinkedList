# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake_first_node = ListNode()
        fake_first_node.next = head

        probe = head
        prev = fake_first_node

        while probe:

            if probe.next and probe.val == probe.next.val:
                val = probe.val

                while probe and probe.val == val:
                    probe = probe.next

                prev.next = probe

            else:
                prev = probe
                probe = probe.next

        return fake_first_node.next
