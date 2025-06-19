# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(cur, level):
            if cur is None:
                return

            if len(output) < level:
                output.append([cur.val])
            else:
                output[level-1].append(cur.val)

            traverse(cur.left, level+1)
            traverse(cur.right, level+1)
            
        
        output = []
        traverse(root, 1)
        
        return output[::-1]
