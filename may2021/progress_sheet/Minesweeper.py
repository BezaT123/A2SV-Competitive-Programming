"""
board = [
["B","1","E","1","B"],
["B","1","M","1","B"],
["B","1","1","1","B"],
["B","B","B","B","B"]], 

click = [3,0]


["B","1","E","1","B"],
["B","1","x","1","B"],
["B","1","1","1","B"],
["B","B","B","B","B"]

"""



class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        visited = set()
        self.revealBoard(board, click,visited)
        return board
    
    
    def revealBoard(self, board, click, visited):
        visited.add(tuple(click))
        
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return
        if board[click[0]][click[1]] == "E":
            valid_neigh, num_neigh_mines = self.getValidNeigh(board,click[0],click[1])
            
            if num_neigh_mines == 0:
                board[click[0]][click[1]] = "B"
                for neigh in valid_neigh:
                    if tuple(neigh) in visited:
                        continue
                    self.revealBoard(board,neigh,visited)
            else:
                board[click[0]][click[1]] = str(num_neigh_mines)
    
    def getValidNeigh(self, board, r, c):
        neigh_list = []
        num_of_mines = 0
            
        for direction in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]:
            neigh_row = r + direction[0]
            neigh_col = c + direction[1]
            
            if 0 <= neigh_row < len(board) and 0 <= neigh_col < len(board[r]):
                neigh_list.append([neigh_row, neigh_col])
                if board[neigh_row][neigh_col] == "M":
                    num_of_mines += 1
                    
        return neigh_list,num_of_mines
                    
  
