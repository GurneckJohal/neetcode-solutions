class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.matrix_prefixes = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                self.matrix_prefixes[i+1][j+1] = matrix[i][j] + self.matrix_prefixes[i][j+1] + self.matrix_prefixes[i+1][j] - self.matrix_prefixes[i][j]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix_prefixes[row2+1][col2+1] - self.matrix_prefixes[row2+1][col1] - self.matrix_prefixes[row1][col2+1] +  self.matrix_prefixes[row1][col1] 

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)