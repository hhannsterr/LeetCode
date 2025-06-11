class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def gen(arr):
            output = [1]
            length = len(arr)
            if length >= 2:
                for i in range(0, len(arr)-1):
                    output.append(arr[i] + arr[i+1])
            output.append(1)
            return output

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            temp = [1]
            for i in range(rowIndex):
                temp = gen(temp)
            return temp