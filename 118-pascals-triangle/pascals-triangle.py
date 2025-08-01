class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def gen(num, arr):
            output = [1]
            last_arr = arr[-1]
            for i in range(len(last_arr)-1):
                output.append(last_arr[i] + last_arr[i+1])
            output.append(1)
            return output


        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]

        triangle = [[1], [1,1]]
        for i in range(3, numRows+1):
            triangle.append(gen(i, triangle))

        return triangle

        


















        # def gen(arr):
        #     output = [1]
        #     length = len(arr)
        #     if length >= 2:
        #         for i in range(0,length-1):
        #             output.append(arr[i]+arr[i+1])
        #     output.append(1)
        #     return output

        # arr = []
        # output = [[1]]
        # for i in range(1,numRows):
        #     arr = gen(arr)
        #     output.append(arr)
        # return output
