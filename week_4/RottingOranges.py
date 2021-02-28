from typing import List, Deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        directional = [[0,1],[0,-1],[1,0],[-1,0]]
        que = Deque()
        count = -1
        
        
        found_rotten = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    que.append([i,j])
                    found_rotten = True
                    
        
        while que:
            size = len(que)
            count += 1
            for i in range(size):
                x = que.popleft()
                for j in range(len(directional)):
                    child_i =  x[0] + directional[j][0]
                    child_j = x[1] + directional[j][1]
                    
                    if 0 <= child_i < m and 0 <= child_j < n:
                        if grid[child_i][child_j] == 1:
                            grid[child_i][child_j] = 2
                            que.append([child_i, child_j])

        
        has_fresh = False
        for i in grid:
            if 1 in i:
                has_fresh = True
        
        if not has_fresh:
            if found_rotten:
                return count
            return 0
        return -1