class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def gen(arr):
            output = [1]
            length = len(arr)
            if length >= 2:
                for i in range(0,length-1):
                    output.append(arr[i]+arr[i+1])
            output.append(1)
            return output

        arr = []
        output = [[1]]
        for i in range(1,numRows):
            arr = gen(arr)
            output.append(arr)
        return output

