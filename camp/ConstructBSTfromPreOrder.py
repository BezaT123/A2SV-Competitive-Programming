# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        stack = []
        root = TreeNode()
        lb = 0
        ub = 10 ** 8 + 1
        
        for i in preorder:
            new_node = TreeNode(i)
            
            if len(stack) == 0:
                root.left = new_node
            else:
                bound_l = self.findBoundFromStack(stack,i)
                parent = bound_l[1]
                
                if i > parent.val:
                    parent.right = new_node 
                else:
                    parent.left = new_node
                    
                lb = bound_l[0][0]
                ub = bound_l[0][1]

                
                
            stack.append([(new_node.val,ub),new_node])
            stack.append([(lb,new_node.val),new_node])
        
        return root.left
        
    def findBoundFromStack(self,stack,i):
        elem = []
        while len(stack) != 0:
            elem = stack.pop()
            if elem[0][0] < i < elem[0][1]:
                break
        return elem
        
    
