# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        t3 = TreeNode()
        return self.merge(t1,t2,t3)
        
    def merge(self, t1: TreeNode, t2: TreeNode, t3: TreeNode):
        
        if t1 == None and t2 == None:
            t3 = None
        elif t1 == None:
            t3 = t2
        elif t2 == None:
            t3 = t1
        else:
            
            t3.val = t2.val + t1.val
            t3.left = self.merge(t1.left,t2.left,TreeNode())
            t3.right = self.merge(t1.right,t2.right,TreeNode())
        return t3