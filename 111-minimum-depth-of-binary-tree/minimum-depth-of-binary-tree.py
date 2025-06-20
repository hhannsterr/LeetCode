# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(cur, height):
            if cur is None:
                return
            if cur.left is None and cur.right is None:
                heights.append(height)
            else:
                traverse(cur.left, height+1)
                traverse(cur.right, height+1)

        heights = []    
        traverse(root, 1)

        if heights == []:
            return 0
        else:
            return min(heights)
            
