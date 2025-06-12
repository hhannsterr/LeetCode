class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for row in range(len(triangle)-2, -1, -1):
            next_row = triangle[row+1]
            for i in range(row + 1):
                triangle[row][i] += min(next_row[i], next_row[i+1])
        return triangle[0][0]
