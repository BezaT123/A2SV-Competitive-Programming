# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        l = []
        self.postOrder(root,l)
        return l
    
    def postOrder(self,root,l):
        if root == None:
            return
        self.postOrder(root.left, l)
        self.postOrder(root.right, l)
        l.append(root.val)

