class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def in_row(row, target):
            return target >= row[0] and target <= row[-1]
        
        def binary_search_v(matrix, target, start, end):
            if start >= end:
                return start
            mid = (start + end) // 2
            if target == matrix[mid][0]:
                return mid
            elif target > matrix[mid][0]:
                if in_row(matrix[mid], target):
                    return mid
                return binary_search_v(matrix, target, mid+1, end)
            else:
                return binary_search_v(matrix, target, start, mid-1)

        def binary_search_h(row, target, start, end):
            if start > end:
                return False
            mid = (start + end) // 2
            if target == row[mid]:
                return True
            elif target > row[mid]:
                return binary_search_h(row, target, mid+1, end)
            else:
                return binary_search_h(row, target, start, mid-1)
        
        if len(matrix) > 1:
            row = binary_search_v(matrix, target, 0, len(matrix)-1)
        else:
            row = 0
        return binary_search_h(matrix[row], target, 0, len(matrix[0])-1)
