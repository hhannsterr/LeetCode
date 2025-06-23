class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        def get_ascii(number):
            return chr(number+64)
        
        # A = 65, Z = 90
        output = ''
        whole, remain = columnNumber // 26, columnNumber % 26
        if remain == 0:
            whole, remain = whole-1, 26
        while whole != 0:
            output = get_ascii(remain) + output
            whole, remain = whole // 26, whole % 26
            if remain == 0:
                whole, remain = whole-1, 26
        
        return get_ascii(remain) + output
