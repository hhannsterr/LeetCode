"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def traverse(cur):
            if cur is None:
                return
            if cur.left:
                cur.left.next = cur.right
            if cur.next and cur.right:
                cur.right.next = cur.next.left

            traverse(cur.left)
            traverse(cur.right)

        traverse(root)
        return root
