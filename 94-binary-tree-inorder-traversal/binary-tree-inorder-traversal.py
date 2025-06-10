# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        global_output = []
        def traverse(root):
            if not root:
                return
            
            if root.left != None:
                traverse(root.left)
            
            global_output.append(root.val)
            
            if root.right != None:
                traverse(root.right)
        
        traverse(root)
        return global_output

