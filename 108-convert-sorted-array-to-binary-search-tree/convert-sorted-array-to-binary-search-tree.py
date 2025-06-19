# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def binary_search(arr, start, end):
            if start > end:
                return
            mid = (start + end) // 2
            
            return TreeNode(
                val = arr[mid],
                left = binary_search(arr, start, mid-1),
                right = binary_search(arr, mid+1, end)
            )

        return binary_search(nums, 0, len(nums)-1)

        
