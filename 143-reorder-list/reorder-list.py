# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def get_mid(head):
            slow = head
            fast = head

            while fast.next:
                if fast.next.next:
                    fast = fast.next.next
                else:
                    fast = fast.next
                slow = slow.next
            
            return slow

        def reverse(head):
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


        if not head:
            return head
        
        if not head.next:
            return head

        if not head.next.next:
            return head

        mid = get_mid(head)
        end = reverse(mid)

        
        node = ListNode()
        curr = node
        while head and end:
            if head:
                curr.next = head
                head = head.next
                curr = curr.next
            if end.next:
                curr.next = end
                end = end.next
                curr = curr.next

        return node.next
            
