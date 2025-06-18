# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        cur = head
        store = []
        start_storing = False
        for cnt in range(1, right+1):
            if start_storing:
                store.append(cur.val)
            if cnt == left:
                left_node = cur
                start_storing = True
            elif cnt == right:
                right_node = cur
                store.pop()
                break
            cur = cur.next
        
        left_node.val, right_node.val = right_node.val, left_node.val
        left_node = left_node.next
        
        while left_node != right_node:
            left_node.val = store.pop()
            left_node = left_node.next
            
        return head