class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        # print(len(grid), len(grid[190]))
        return self.minPathSumDFS(grid, dp, 0,0)
    
    def minPathSumDFS(self, grid, dp, row, column):
                
        if row == len(grid) - 1 and column == len(grid[0]) - 1:
            return grid[row][column]
        
        if not self.inBound(grid, row, column):
            return 10 ** 5
        
        if (row, column) in dp:
            return dp[(row,column)]

        value = grid[row][column]
        
        down = self.minPathSumDFS(grid, dp, row + 1, column)
        right = self.minPathSumDFS(grid, dp, row, column + 1)
        
        value += min(down,right)
        dp[(row,column)] = value
        return dp[(row,column)]
    
    def inBound(self, grid, row, column):
        if 0 <= row < len(grid) and 0 <= column < len(grid[0]):
            return True
        return False
