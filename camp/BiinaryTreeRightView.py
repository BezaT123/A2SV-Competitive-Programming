# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, result, depth):
        if not root:
            return
        if len(result) == depth:
            result.append(root.val)
            
        else:
            print(result[depth],root.val)
            result[depth] = root.val
            
        self.dfs(root.left, result, depth + 1)
        self.dfs(root.right, result, depth + 1)
        

    
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []
        self.dfs(root,result,0)
        return result
