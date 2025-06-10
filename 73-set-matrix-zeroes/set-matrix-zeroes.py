class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()
        num_row = len(matrix)
        num_col = len(matrix[0])
        
        for i in range(num_row):
            for j in range(num_col):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        
        for i in row:
            for j in range(num_col):
                matrix[i][j] = 0

        for j in col:
            for i in range(num_row):
                matrix[i][j] = 0
