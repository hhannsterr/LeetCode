# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(self, cur_sum):
            if not self:
                return False
            cur_sum += self.val
            if not self.left and not self.right:
                return cur_sum == targetSum
            return traverse(self.left, cur_sum) or traverse(self.right, cur_sum)
        
        return traverse(root, 0)
