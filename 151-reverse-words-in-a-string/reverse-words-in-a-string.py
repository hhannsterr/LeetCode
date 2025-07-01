class Solution:
    def reverseWords(self, s: str) -> str:
        output = ''
        temp = ''
        s = s.strip() + ' '
        prev_spacebar = False
        for letter in s:
            if letter == ' ':
                if not prev_spacebar:
                    output = temp + ' ' + output
                    temp = ''
                prev_spacebar = True
            else:
                temp += letter
                prev_spacebar = False
        
        return output[:-1]
