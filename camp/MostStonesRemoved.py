def removeStonesk(stones):
    graph = {}
    for i in range(len(stones)):
        graph[stones[i]] = []
        for j in range(i+1,len(stones)):
            if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                graph[stones[i]].append(stones[j])
    
    print(graph)

removeStones([[0,0],[0,1],[1,0],[1,2]])