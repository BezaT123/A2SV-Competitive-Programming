# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        return self.add(root,low,high,0)
        
    def add(self, root: TreeNode, low: int, high: int, sums : int):
        if root == None:
            return sums
        if root.val >= low and root.val <= high:
            sums += root.val
        sums = self.add(root.left,low,high,sums)
        sums = self.add(root.right,low,high,sums)
        return sums