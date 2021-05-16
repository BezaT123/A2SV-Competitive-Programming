"""

graph= [
0 :[1,2,3]
1: [0,2],
2: [0,1,3]
3: [0,2]
]
[r,b,b,b]

[
[1,3]
[0,2]
[1,3,4,5]
[0,2]
[2,5]
[4,2]]

[1,-1,1,-1,-1,-1]

[1]
[]

[[1],[0,3],[3],[1,2]]
[r,b,b,r]
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()
        check_partite = [0] * len(graph)
        isBipartite = True
        
        for i in range(len(graph)):
            if i not in visited:
                check_partite[i] = 1
                isBipartite = isBipartite and self.dfsCheckPartite(graph, i, visited, check_partite)
                if not isBipartite:
                    return isBipartite
        return True
    
    def dfsCheckPartite(self, graph, i, visited, check_partite):
        val_i = check_partite[i]
        visited.add(i)
        partite = True
        for j in graph[i]:
            if check_partite[j] == val_i:
                return False
            if check_partite[j] == 0:
                check_partite[j] = val_i * -1
            
        for j in graph[i]:    
            if j in visited:
                continue
            partite = partite and self.dfsCheckPartite(graph, j, visited, check_partite)
            if not partite:
                return False
        return True
        
        
        
