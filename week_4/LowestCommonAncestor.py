# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # l = []
        # self.appendAncestors(root,p,q,l)
        # l.sort()
        # print(l[0])
        if (root.val >= p.val and root.val <= q.val) or (root.val >= q.val and root.val <= p.val):
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)