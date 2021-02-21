# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.dfs(root,1,1)
    
    def dfs(self,root,parent,grandparent):
        sum = 0
        
        if not root:
            return 0
        
        sum = self.dfs(root.left, root.val, parent) + self.dfs(root.right, root.val, parent)
        
        if grandparent % 2 == 0:
            sum += root.val
            
        return sum