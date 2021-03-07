# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.findKthSmallest(root, 0, k)[0]
    
    def findKthSmallest(self, node, index, k):
        if node.left:
            index, found = self.findKthSmallest(node.left, index, k)
            if found:
                return index, True
            
        index = index + 1
        
        if index == k:
            return node.val, True
        
        if node.right:
            index,found = self.findKthSmallest(node.right, index, k)   
            if found:
                return index, True
        return index, False