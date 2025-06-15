# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_tail_and_length(cur):
            if cur is None:
                return cur, 0
            cnt = 1
            while cur.next:
                cnt += 1
                cur = cur.next
            return cur, cnt
        
        if k == 0:
            return head

        tail, length = get_tail_and_length(head)
        if length == 0:
            return

        tail.next = head
        k = k % length

        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        output = cur.next
        cur.next = None
        
        return output
