# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.checkValidBST(root, -1 * (2 ** 31) -1, (2 ** 31))
    
    def checkValidBST(self, root, lb, ub):
        if lb < root.val < ub:
            left_val = right_val = True
            if root.left:
                left_val = self.checkValidBST(root.left, lb, root.val)
            if root.right:
                right_val = self.checkValidBST(root.right, root.val, ub)
            return left_val and right_val
        return False
        