class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        curr_diag = 0
        max_area = 0
        for l, w in dimensions:
            next_diag = l*l + w*w
            if next_diag == curr_diag:
                max_area = max(max_area, l*w)
            elif next_diag > curr_diag:
                curr_diag = next_diag
                max_area = l*w
            
        return max_area
