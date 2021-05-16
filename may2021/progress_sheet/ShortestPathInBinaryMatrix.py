"""
deal with case -1
 if [0][0] == 1 or [n-1][n-1] == 1
 if last_visited cell before que ends is not [n-1][n-1]
 
last_visited = []
append to que 0,0
start level = 1
    pop from que
    set last_visted to popped elem
    append its children:
        if children == [n-1][n-1]:
            break
        change children value to 1 # mark it as visited
    increment level
    

"""


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1 or grid[len(grid)-1][len(grid)-1] == 1:
            return -1
        
        last_visited = []
        que = Deque()
        que.append([0,0])
        length = 0
        
        while que:
            length += 1
            size = len(que)
            for i in range(size):
                cell = que.popleft()
                last_visited = cell
                grid[cell[0]][cell[1]] = 1
                if cell == [len(grid)-1, len(grid)-1]:
                    return length
                for direction in [[0,1],[0,-1],[1,0],[-1,0],[-1,1],[1,-1],[1,1],[-1,-1]]:
                    neigh_i = cell[0] + direction[0]
                    neigh_j = cell[1] + direction[1]
                    
                    if 0 <= neigh_i < len(grid) and 0 <= neigh_j < len(grid):
                        
                        if grid[neigh_i][neigh_j] == 0:
                            # add the neighbors, change val to 1
                            que.append([neigh_i, neigh_j])
                            grid[neigh_i][neigh_j] = 1
                # print(length, last_visited)
        if last_visited == [len(grid)-1, len(grid)-1]:
            return length
        return -1
        
