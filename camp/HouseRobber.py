class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        
        if len(nums) == 1:
            return nums[0]
        
        return max(self.maxSumRobbing(nums, dp, 0), self.maxSumRobbing(nums, dp, 1))
    
    def maxSumRobbing(self, nums, dp, ind):

        if ind == len(nums) - 1 or ind == len(nums) - 2:
            dp[ind] = nums[ind]
            return dp[ind]
        
        if ind >= len(nums):
            return -1
        
        if dp[ind] != -1:
            return dp[ind]
        
        current = nums[ind]
        
        option_1 = self.maxSumRobbing(nums, dp, ind + 2)
        option_2 = self.maxSumRobbing(nums, dp, ind + 3)

        dp[ind] = current + max(option_1, option_2)
        
        return  dp[ind]
