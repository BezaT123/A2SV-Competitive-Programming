"""
capture - find all 0s surrounded by Xs
        - change them to Xs
        
    
[
["O","O","O","O"],
["X","O","O","X"],
["X","X","O","X"],
["X","O","X","X"]
]
[
["O","X","X","O"],
["X","O","O","X"],
["X","X","O","X"],
["X","O","O","X"]
]

[
["X","O","X","O","X","O"]
["O","X","O","X","O","X"]
["X","O","X","O","X","O"]
["O","X","O","X","O","X"]
]
[
["X","O","X","O","X","O"]
["O","X","X","X","X","X"]
["X","X","X","X","X","O"]
["O","X","O","X","O","X"]
]
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if tuple([i,j]) in visited:
                    continue
                if (i == 0 or i == len(board) -1) or (j == 0 or j == len(board[i])-1):
                    # print(i,j)
                    if board[i][j] == "O":
                        self.changeConnectedO(board, i, j, visited, True)
                    
        for i in range(len(board)):
            for j in range(len(board[i])):
                
                if tuple([i,j]) not in visited:
                    if board[i][j] == "O":
                        self.changeConnectedO(board, i, j, visited, False)
                            
                            
    def changeConnectedO(self,board, i, j, visited, boarder_o):
        visited.add(tuple([i,j]))
        if not boarder_o:
            board[i][j] = "X"
        
        # call for valid neighbors
        for direction in [[-1,0],[1,0],[0,1],[0,-1]]:
            neigh_i = i + direction[0]
            neigh_j = j + direction[1]
            # valid neighbhor
            if neigh_i < 0 or neigh_i >= len(board) or neigh_j < 0 or neigh_j >= len(board[i]):
                continue
            if board[neigh_i][neigh_j] == "X":
                continue
            if tuple([neigh_i, neigh_j]) in visited:
                continue

            self.changeConnectedO(board,neigh_i, neigh_j, visited,boarder_o)
