# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        current = head

        while current:
            stack.append(current.val)
            current = current.next

        dummy = ListNode(0)

        current = dummy

        while stack:
            current.next = ListNode(stack.pop())
            current = current.next

        return dummy.next

        