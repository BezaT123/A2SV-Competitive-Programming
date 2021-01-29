# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums == []:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        # if type(nums) != type([]):
        #     return nums
        max_indx = 0
        # print(nums)
        for i in range(1,len(nums)):
            if nums[max_indx] < nums[i]:
                max_indx = i
        c = TreeNode(nums[max_indx])
        c.left = self.constructMaximumBinaryTree(nums[0:max_indx])
        c.right = self.constructMaximumBinaryTree(nums[max_indx + 1:])        
        return c