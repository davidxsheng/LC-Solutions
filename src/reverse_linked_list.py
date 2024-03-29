# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode | None = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        else:
            next_node = head.next
            temp_node = self.reverseList(next_node)
            next_node.next = head
            head.next = None

            return temp_node
