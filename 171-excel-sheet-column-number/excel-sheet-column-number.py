class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        def get_num(letter):
            return ord(letter) - 64

        
        if len(columnTitle) == 1:
            return get_num(columnTitle)
        
        temp = columnTitle[::-1]
        output = 0
        power = 1
        for i in range(len(temp)):
            output += get_num(temp[i])*power
            power *= 26
        return output
