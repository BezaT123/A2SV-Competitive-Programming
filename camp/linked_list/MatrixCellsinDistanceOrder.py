class Solution:
    
    def findNeighbors(self, x, y, R, C, visited):
        result = []
        direction = [(0,1) , (0,-1), (1,0), (-1,0)]
        for i in direction:
            adj_x = x + i[0]
            adj_y = y + i[1]
            if  0 <= adj_x < R and 0 <= adj_y < C and (adj_x,adj_y) not in visited:
                result.append([adj_x,adj_y])
        return result
    
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        result = []
        visited = set()
        que = deque()
        que.append([r0,c0])
        
        while len(que) != 0:
            size = len(que)
            for i in range(size):
                x = que.popleft()
                if tuple(x) in visited:
                    continue
                visited.add(tuple(x))
                result.append(x)
                for i in self.findNeighbors(x[0], x[1], R, C, visited):
                    if tuple(i) not in visited:
                        que.append(i)

        return result