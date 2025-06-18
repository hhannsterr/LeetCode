# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = ListNode(val=0, next=None)
        more_head = ListNode(val=0, next=None)
        
        cur = head
        less = less_head
        more = more_head
        
        while cur:
            if cur.val < x:
                less.next = cur
                less = less.next
            else:
                more.next = cur
                more = more.next
            cur = cur.next
        
        less.next = more_head.next
        more.next = None

        return less_head.next
