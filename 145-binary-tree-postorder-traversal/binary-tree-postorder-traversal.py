# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(cur):
            if cur is None:
                return
            
            if cur.left:
                traverse(cur.left)
            if cur.right:
                traverse(cur.right)

            output.append(cur.val)

        output = []
        traverse(root)
        return output
