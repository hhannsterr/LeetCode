# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        
        prev = head
        cur = head.next
        while cur != None:
            if prev.val != cur.val:
                prev.next = cur
                prev = cur
            if cur.next == None:
                prev.next = None
                return head
            cur = cur.next
        
        return head
        