# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # cur = head
        # nums = []
        # while cur:
        #     nums.append(cur.val)
        #     cur = cur.next

        # new_head = ListNode()
        # cur = new_head
        # while nums:
        #     cur.next = ListNode(nums.pop())
        #     cur = cur.next

        # return new_head.next
        
        if not head:
            return
        
        if not head.next:
            return head

        prev = head
        curr = head.next
        prev.next = None
        
        while curr.next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        curr.next = prev
        return curr
