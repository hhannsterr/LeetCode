# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def traverse(cur, path, paths):
            if cur is None:
                return

            path.append(cur.val)

            if cur.left is None and cur.right is None:
                if sum(path) == targetSum:
                    paths.append(list(path))
            else:
                traverse(cur.left, path, paths)
                traverse(cur.right, path, paths)
            path.pop()
        
        paths = []
        traverse(root, [], paths)
        
        return paths
