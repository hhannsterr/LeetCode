class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def spiral(starting_number, layer, output, n):
            for col in range(layer, n-layer):
                output[layer][col] = starting_number
                starting_number += 1
            
            for row in range(layer+1, n-layer):
                output[row][-layer-1] = starting_number
                starting_number += 1
            
            for col in range(n-layer-2, layer-1, -1):
                output[n-layer-1][col] = starting_number
                starting_number += 1
            
            for row in range(n-layer-2, layer, -1):
                output[row][layer] = starting_number
                starting_number += 1
            
            return starting_number, output

        def final_for_odd(starting_number, output, mid):
            mid = n // 2
            output[mid][mid] = starting_number

            return output
        

        output = [ [0] * n for _ in range(n) ]
        mid = n // 2
        num = 1

        for layer in range(mid):
            num, output = spiral(num, layer, output, n)

        if n % 2 == 0:
            return output
        else:
            return final_for_odd(num, output, mid)
