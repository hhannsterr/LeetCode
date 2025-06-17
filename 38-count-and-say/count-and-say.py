class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(string):
            pre = string[0]
            cnt = 1
            output = ''
            for num in string[1:]:
                if pre == num:
                    cnt += 1
                else:
                    output += str(cnt) + pre
                    pre = num
                    cnt = 1
            output += str(cnt) + pre
            return output
        

        if n == 1:
            return '1'
        elif n == 2:
            return '11'

        string = '11'
        for i in range(2, n):
            string = rle(string)
        return string
        