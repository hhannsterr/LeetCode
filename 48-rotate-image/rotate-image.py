class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """        
        # [ 0 ][ 0 ] [ 0 ][ 1 ] [ 0 ][ 2 ] [ 0 ][ 3 ]
        # [ 0 ][n-1] [ 1 ][n-1] [ 2 ][n-1] [ 3 ][n-1]
        # [n-1][n-1] [n-1][n-2] [n-1][n-3] [n-1][n-4]
        # [n-1][ 0 ] [n-2][ 0 ] [n-3][ 0 ] [n-4][ 0 ]

        # [ 1 ][ 1 ] 
        # [ 1 ][n-2] 
        # [n-2][n-2] 
        # [n-2][ 1 ] 

        def replace_layer(matrix, layer, length):
            for i in range(layer, length-layer-1):
                temp = matrix[layer][i]
                matrix[layer][i] = matrix[length-i-1][layer]
                matrix[length-i-1][layer] = matrix[length-layer-1][length-i-1]
                matrix[length-layer-1][length-i-1] = matrix[i][length-layer-1]
                matrix[i][length-layer-1] = temp
        
        length = len(matrix)
        for layer in range(length // 2):
            replace_layer(matrix, layer, length)
        