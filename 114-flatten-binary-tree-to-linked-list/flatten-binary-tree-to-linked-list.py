# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traverse(cur):
            if cur is None:
                return
            store.append(cur.val)
            traverse(cur.left)
            traverse(cur.right)

        def flat(cur):
            cur.left = None
            store.pop()
            while store:
                cur.right = TreeNode(store.pop())
                cur = cur.right

        
        if root is None:
            return
        
        store = []
        traverse(root)
        store = store[::-1]
        flat(root)
                