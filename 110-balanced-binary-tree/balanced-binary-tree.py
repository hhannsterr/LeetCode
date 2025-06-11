# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        if root is None:
            return True

        def height(root):
            if root is None:
                return -1

            lheight = height(root.left)
            rheight = height(root.right)

            return max(lheight, rheight) + 1

        def inorder_height(root):
            if root is None:
                return True

            # Check left subtree
            if not inorder_height(root.left):
                return False

            # Check current node's balance
            lheight = height(root.left)
            rheight = height(root.right)
            if abs(lheight - rheight) > 1:
                return False

            # Check right subtree
            if not inorder_height(root.right):
                return False

            return True

        return inorder_height(root)
            

        

