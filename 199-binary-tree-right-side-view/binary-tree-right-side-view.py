# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(curr, height):
            if curr is None:
                return

            if height not in hash_map:
                hash_map[height] = curr.val

            traverse(curr.right, height+1)
            traverse(curr.left, height+1)

        
        hash_map = {}

        curr = root
        traverse(curr, 0)

        return list(hash_map.values())
        