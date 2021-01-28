# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q:
            return False
        elif q == None and p:
            return False
        elif p and q:
            if p.val != q.val:
                return False
            if not self.isSameTree(p.left,q.left):
                return False
            if not self.isSameTree(p.right,q.right):
                return False
        return True