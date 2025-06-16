# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not(head and head.next):
            return head

        prev = head
        curr = head.next
        
        cont = True
        while cont:
            prev.val, curr.val = curr.val, prev.val
            if curr.next and curr.next.next:
                prev = curr.next
                curr = curr.next.next
            else:
                cont = False

        return head
