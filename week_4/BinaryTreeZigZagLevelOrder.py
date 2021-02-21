# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        result = []
        dque = deque([root])
        left = True
        
        while dque:
            size = len(dque)
            level = []
            children = []

            for i in range(size):
                node = dque.pop()
                if left:
                    if node.left:
                        children.append(node.left)

                    if node.right:
                        children.append(node.right)

                else:
                    if node.right:
                        children.append(node.right)
                    
                    if node.left:
                        children.append(node.left)
                        
                level.append(node.val)
                
                
            dque = deque(children)
            left = not left 
            result.append(level)
        return result