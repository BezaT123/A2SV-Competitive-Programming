class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # bottom up
        """dp = {}
        
        for i in range(len(triangle) - 1, -1, -1):
            for j in range(len(triangle[i])):
                if i == len(triangle) - 1:
                    dp[(i,j)] = triangle[i][j]
                    
                else:
                    dp[(i,j)] = triangle[i][j] + min(dp[(i + 1,j)], dp[(i + 1, j +1)])
        
        # print(dp)
        
        return dp[(0,0)]"""

        # top down
        dp  = {}
        return self.minimumTotalDFS(triangle,dp,0,0)
    
    
    def minimumTotalDFS(self, triangle, dp,row, column):
        
        if row == len(triangle) - 1:
            return triangle[row][column]
        
        
        if (row, column) in dp:
            
            return dp[(row, column)]
        
        value = triangle[row][column]
        
        left = self.minimumTotalDFS(triangle,dp, row + 1, column)
        right = self.minimumTotalDFS(triangle,dp, row + 1, column + 1)
        
        value += min(left,right)
        dp[(row,column)] = value
        return value

        
