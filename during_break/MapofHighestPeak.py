from typing import Deque, List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        visited = set([])
        que = Deque([])
        directions =[[0,1], [1,0], [-1,0], [0,-1]]

        m = len(isWater)
        n = len(isWater[0])
        result = [[-1] * m] * n

        adjecent = ()
        que.append([0,0],[m-1,n-1],[0,n-1],[m-1,0])

        while que:
            x = que.pop()
            i = x[0]
            j = x[1]
            if x in visited:
                continue
            if isWater[i][j] == 1:
                result[i][j] = 0
                visited.append(x)
                for i in directions:
                    if 0 <= x[0] + i[0] <= m and 0 <= x[1] + i[1] <= n:
                        que.append([x[0] + i[0], x[1] + i[1]])
                        adjecent = (x,[x[0] + i[0], x[1] + i[1]])
                        
            else:
                adjecent = []
                min = 10 ** 6
                adj_has_height = False
                my_options = []
                for i in range(4):
                    if 0 <= x[0] + i[0] <= m and 0 <= x[1] + i[1] <= n:
                        adj = [x[0] + i[0], x[1] + i[1]]
                        if result[adj[0]][adj[1]] != -1:
                            adj_has_height = True
                            if result[adj[0]][adj[1]] < min:
                                min = result[adj[0]][adj[1]]
                if adj_has_height:
                    result[x[0]][x[1]] = min + 1
                    visited.append(x)
                    for i in directions:
                        if 0 <= x[0] + i[0] <= m and 0 <= x[1] + i[1] <= n:
                            que.append([x[0] + i[0], x[1] + i[1]])
                else:
                    visited.append(x)
                    for i in directions:
                        if 0 <= x[0] + i[0] <= m and 0 <= x[1] + i[1] <= n:
                            que.append([x[0] + i[0], x[1] + i[1]])
                    que.append(x)
        return result
                
                


