"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if not root:
            return 0
        
        max_child = 0
        for i in root.children:
            x = self.maxDepth(i)
            if max_child < x:
                max_child = x
        return max_child + 1
