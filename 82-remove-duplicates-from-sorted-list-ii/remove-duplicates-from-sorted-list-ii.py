# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        new_head = ListNode(val = 1000, next = head)
        temp = new_head
        while cur and cur.next:
            if cur.val != cur.next.val:
                if temp.next == cur or temp == cur:
                    temp = cur
                else:
                    temp.next = cur.next
            elif cur.next.next is None:
                temp.next = None
            cur = cur.next

        return new_head.next
        