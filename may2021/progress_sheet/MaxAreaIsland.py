"""
max_area = 0
island: no_of_cells

iterate over the grid, i, j:
    if 0s: continue:
    if 1:
        call dfs(grid, i,j, num_cell=0)
        if max_area < num_cell:
            max_area = num_cell
        
        
dfs(num_cell):    
    add 1 to num_cell
    change to 0
        iterate and check negigbhors:
            if negihgbor == 1:
                call the dfs(num_cells)
                
                
                


"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                if grid[i][j] == 0:
                    continue
                else:
                    num_cells = [0]
                    self.dfsFindNumCells(grid, i, j, num_cells)
                    max_area = max(num_cells[0], max_area)
        return max_area
    
    def dfsFindNumCells(self, grid, i, j, num_cells):
        num_cells[0] += 1
        grid[i][j] = 0
        
        for direction in [[0,1],[0,-1],[1,0],[-1,0]]:
            neigh_i = i + direction[0]
            neigh_j = j + direction[1]
            if 0 <= neigh_i < len(grid) and 0 <= neigh_j < len(grid[i]):
                if grid[neigh_i][neigh_j] == 1:
                    self.dfsFindNumCells(grid, neigh_i, neigh_j,num_cells)
