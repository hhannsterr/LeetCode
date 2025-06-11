# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def checkNode(root):
            if root is None:
                return 'N'
            else:
                return root.val

        def checkMirror(root_1, root_2, result):
            val_1 = checkNode(root_1)
            val_2 = checkNode(root_2)

            if val_1 != val_2:
                result = False
            else:
                if root_1.left or root_2.right:
                    result = checkMirror(root_1.left, root_2.right, result)
                if root_1.right or root_2.left:
                    result = checkMirror(root_1.right, root_2.left, result)

            return result
                    
        
        if root.left is None and root.right is None:
            return True
        else:
            return checkMirror(root.left, root.right, True)
        