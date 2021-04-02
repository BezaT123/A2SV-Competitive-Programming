class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * len(cost)
        return min(self.minCostDFS(cost,dp,0), self.minCostDFS(cost,dp,1))
        
    
    def minCostDFS(self, cost, dp, ind):
        
        if ind == len(cost) - 1 or ind == len(cost) - 2:
            return cost[ind]
        
        if dp[ind] != -1:
            return dp[ind]
        
        left = self.minCostDFS(cost, dp, ind + 1)
        right = self.minCostDFS(cost, dp,  ind + 2)
        
        dp[ind] = cost[ind] + min(left, right)
        
        return dp[ind]
