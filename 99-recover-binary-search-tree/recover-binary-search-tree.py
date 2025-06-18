# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """        
        def traverse_store(cur):
            if cur is None:
                return
            if cur.left:
                traverse_store(cur.left)
            
            store.append(cur.val)
            
            if cur.right:
                traverse_store(cur.right)

        def traverse_replace(cur, swap_1, swap_2):
            if cur is None: 
                return 
            if cur.left:
                traverse_replace(cur.left, swap_1, swap_2)
            
            if cur.val == swap_1:
                cur.val = swap_2
            elif cur.val == swap_2:
                cur.val = swap_1
                return
            
            if cur.right:
                traverse_replace(cur.right, swap_1, swap_2)

            
        store = []
        traverse_store(root)

        cnt_wrong = 0
        first = None
        for i in range(1, len(store)):
            if store[i-1] > store[i]:
                if first is None:
                    first = i-1
                else:
                    second = i
                cnt_wrong += 1
        
        if cnt_wrong == 0:
            return
        elif cnt_wrong == 1:
            traverse_replace(root, store[first], store[first+1])
        else:
            traverse_replace(root, store[first], store[second])
        
        