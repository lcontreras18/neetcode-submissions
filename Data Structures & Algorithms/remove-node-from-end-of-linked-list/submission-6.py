# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head

        for i in range(n):
            curr = curr.next

        if not curr:
            return head.next
        
        temp = head

        while curr and curr.next:
            temp = temp.next
            curr = curr.next
        
        temp.next = temp.next.next

        return head
        


        