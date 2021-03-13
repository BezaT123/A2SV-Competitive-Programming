# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        if self.isLeafNode(root):
            if root.val == targetSum:
                return True
            return False
        left_child = self.hasPathSum(root.left, targetSum - root.val)
        right_child = self.hasPathSum(root.right, targetSum - root.val)
        
        return left_child or right_child

    def isLeafNode(self, node):
        return not node.left and not node.right
