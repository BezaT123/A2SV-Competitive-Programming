# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        l = []
        
        self.preOrderTraversal(root,l)
        minimum = 10 ** 5
        
        for i in range(len(l) - 1):
            if l[i+1] - l[i] < minimum:
                minimum = l[i+1] - l[i]
        return minimum
        
    def preOrderTraversal(self,root,l):
        if not root:
            return
        
        self.preOrderTraversal(root.left,l)
        l.append(root.val)
        self.preOrderTraversal(root.right,l)