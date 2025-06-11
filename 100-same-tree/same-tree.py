# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def checkVal(root):
            if root is None:
                return 'N'
            else:  
                return root.val 

        def checkSame(root_1, root_2, result):
            val_1 = checkVal(root_1)
            val_2 = checkVal(root_2)

            if val_1 != val_2:
                result = False
            else:
                if root_1.left is not None or root_2.left is not None:
                    result = checkSame(root_1.left, root_2.left, result)
                if root_1.right is not None or root_2.right is not None:
                    result = checkSame(root_1.right, root_2.right, result)

            return result

        result = True
        if p is None and q is None:
            return result
        else:
            result = checkSame(p, q, result)
        return result


        