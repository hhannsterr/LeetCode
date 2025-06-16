class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def print_by_layer(matrix, layer, output, row, col):
            num_element = row * col
            
            if len(output) == num_element:
                return output

            for c in range(layer, col-layer):
                output.append(matrix[layer][c])

            if len(output) == num_element:
                return output

            for r in range(1+layer, row-layer):
                output.append(matrix[r][col-layer-1])

            if len(output) == num_element:
                return output

            for c in range(col-layer-2, layer-1, -1):
                output.append(matrix[row-layer-1][c])

            if len(output) == num_element:
                return output
            
            for r in range(row-layer-2, layer, -1):
                output.append(matrix[r][layer])
            
            return output

        
        output = []

        col = len(matrix[0])
        row = len(matrix)

        for i in range(row+1 // 2):
            output = print_by_layer(matrix, i, output, row, col)

        return output
