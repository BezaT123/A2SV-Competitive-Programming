# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        result = []
        que = deque([root])
        
        while que:
            size = len(que)
            total  = count = 0

            for i in range(size):
                node = que.popleft()
                total += node.val
                count += 1
                
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                    
            result.append(total/count)
        return result