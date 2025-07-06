class Solution:
    def kthCharacter(self, k: int) -> str:       
        def helper(letter):
            if letter == 'z':
                return 'a'
            else:
                return chr(ord(letter) + 1)
        
        def operation(string):
            new_string = ''
            for letter in string:
                new_string += helper(letter)
            return string + new_string

        def final_op(string, num):
            return helper(string[num])

        
        if k == 1:
            return 'a'
        
        word = 'a'
        half_k = k / 2
        
        while len(word) < half_k:
            word = operation(word)

        return final_op(word, k-len(word)-1)
