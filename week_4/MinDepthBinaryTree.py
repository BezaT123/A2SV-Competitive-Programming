# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        d = deque()
        if not root:
            return 0
        d.append(root)
        return self.bfs(root,d)
    
    def isLeafNode(self,root):
        return (not root.left and not root.right)
        
    def bfs(self,root,queue):
        level = 1
        # iterate until queue is empty
        # dequeue from queue and check if its leaf node
        # if it's not then enqueue it's children 
        
        while len(queue) != 0:
            size = len(queue)
            
            for i in range(size):
                root = queue.popleft()
                if self.isLeafNode(root):
                    return level
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                
            level += 1
        return level
        
        