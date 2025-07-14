class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        length = len(matrix[0])
        for row in range(len(matrix)):
            r = row-1
            if row == 0:
                for col in range(1, length):
                    matrix[0][col] += matrix[0][col-1]
            else:
                matrix[row][0] += matrix[r][0]
                for col in range(1, length):
                    matrix[row][col] = sum([
                        matrix[row][col], 
                        matrix[r][col], 
                        matrix[row][col-1],
                        -matrix[r][col-1]
                    ])
        
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r = row1 - 1
        c = col1 - 1
        
        if row1 == 0 and col1 == 0:
            return self.matrix[row2][col2]
        elif row1 == 0 and col1 != 0:
            return self.matrix[row2][col2] - self.matrix[row2][c]
        elif row1 != 0 and col1 == 0:
            return self.matrix[row2][col2] - self.matrix[r][col2]
        
        return sum([
            self.matrix[row2][col2], 
            self.matrix[r][c],
            -self.matrix[r][col2],
            -self.matrix[row2][c]
        ])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)