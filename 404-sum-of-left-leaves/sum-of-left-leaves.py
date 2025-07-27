# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def traverse(cur):
            if cur.right:
                if cur.right.right or cur.right.left:
                    traverse(cur.right)
            if cur.left:
                traverse(cur.left)
            if cur.left is None and cur.right is None:
                output.append(cur.val)

        
        if root.left is None and root.right is None:
            return 0

        output = []
        traverse(root)
        
        return sum(output)
            