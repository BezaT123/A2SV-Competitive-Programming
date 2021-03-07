# Definition for a binary tree node.
from typing import Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        que = Deque([])
        
        que.append(root)
        left_child = 0
        while que:
            size = len(que)
            left_child = que[0].val
            for i in range(size):
                x = que.popleft()
                if x.left:
                    que.append(x.left)
                if x.right:
                    que.append(x.right)
        return left_child