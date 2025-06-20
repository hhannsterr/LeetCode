# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def get_length(cur):
            length = 0
            while cur:
                cur = cur.next
                length += 1
            return length

        def get_value(cur, length):
            for i in range(length):
                cur = cur.next
            if cur:
                return cur.val

        def bsa(cur, start, end):
            if start > end:
                return
            mid = (start + end) // 2
            mid_val = get_value(cur, mid)
            root = TreeNode(
                val = mid_val,
                left = bsa(cur, start, mid-1),
                right = bsa(cur, mid+1, end)
            )
            return root

            
        if head is None:
            return

        return bsa(head, 0, get_length(head))

