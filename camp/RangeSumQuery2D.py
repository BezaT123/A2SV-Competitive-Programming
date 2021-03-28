class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        prefix_sum = []
        prev = 0
        for i in matrix:
            l = []
            for j in i:
                prev += j
                l.append(prev)
            prefix_sum.append(l)
            prev = 0
        # print(prefix_sum)
        
        for i in range(1,len(prefix_sum)):
            for j in range(len(prefix_sum[i])):
                prefix_sum[i][j] += prefix_sum[i-1][j]
        
        self.prefix_sum = prefix_sum


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        prev_start_col = self.prefix_sum[row2][col1-1] if col1-1 >=0 else 0
        above_start_row = self.prefix_sum[row1-1][col2] if row1-1 >=0 else 0
        above_start_row_diff = self.prefix_sum[row1-1][col1-1] if row1-1 >=0 and col1-1 >=0 else 0
        
               
        return self.prefix_sum[row2][col2] - prev_start_col - (above_start_row - above_start_row_diff)



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
