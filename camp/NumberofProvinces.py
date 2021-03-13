class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = set([])
        
        for i in range(len(isConnected)):
            if i not in visited:
                # print(i)
                provinces += 1
                self.dfs(isConnected,visited,i)
                
        return provinces
    
    def dfs(self, adj_list, visited,i):
        if i in visited:
            return
        visited.add(i)
        
        for j in range(len(adj_list[i])):
            if adj_list[i][j] != 0:
                self.dfs(adj_list,visited,j)
