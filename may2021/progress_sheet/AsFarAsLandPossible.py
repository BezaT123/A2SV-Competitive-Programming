"""
que -initially all the 1s
iteratively:
    que its neighboring water,
    distance += 1
    
[[1,0,1],[0,0,0],[1,0,1]]
[[1,0,0],[0,0,0],[0,0,0]]
[[1,1,1],[1,1,1],[1,1,1]]
[[0,0,0],[0,0,0],[0,0,0]]
[[1,1,0],[1,1,1],[1,1,1]]
[[1]]
[[0]]
"""



class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        distance = -1
        # visited = set()
        que = Deque()
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    que.append((i,j))
                    
        if len(que) == 0 or len(que) == len(grid) * len(grid):
            return distance
        
        while que:
            size = len(que)
            distance += 1
            # print(que, distance)
            for i in range(size):
                cell = que.popleft()
                
                for direction in [[0,1],[0,-1],[1,0],[-1,0]]:
                    neigh_i = cell[0] + direction[0]
                    neigh_j = cell[1] + direction[1]

                    if 0 <= neigh_i < len(grid) and 0 <= neigh_j < len(grid):

                        if grid[neigh_i][neigh_j] == 0:
                            que.append((neigh_i, neigh_j))
                            grid[neigh_i][neigh_j] = 1
                

            
        return distance
