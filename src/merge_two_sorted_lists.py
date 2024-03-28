from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        previous_node = ListNode()
        new_head = previous_node

        while list1 and list2:
            if list1.val < list2.val:
                previous_node.next = list1
                list1 = list1.next
            else:
                previous_node.next = list2
                list2 = list2.next
            previous_node = previous_node.next

        # Consume the leftover linked list
        if list1:
            previous_node.next = list1
        else:
            previous_node.next = list2

        return new_head.next
