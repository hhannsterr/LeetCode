# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def get_height(root):
            if root is None:
                return 0
            else:
                left_height = get_height(root.left)
                right_height = get_height(root.right)
                if left_height > right_height:
                    return left_height + 1
                else:
                    return right_height + 1

        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        return get_height(root)

