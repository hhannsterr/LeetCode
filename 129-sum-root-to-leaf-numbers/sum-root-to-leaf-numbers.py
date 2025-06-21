# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traverse(cur, path):
            nonlocal summation
            if cur is None:
                return
            path += str(cur.val)
            if cur.left is None and cur.right is None:
                summation += int(path)
            else:
                traverse(cur.left, path)
                traverse(cur.right, path)
            path = path[:-1]

        summation = 0
        traverse(root, '')
        
        return summation
