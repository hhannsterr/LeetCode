class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            return s == s[::-1]

        def gen_substr(s, valid=[]):
            if s == '':
                output.append(valid[:])
                return
            for i in range(1, len(s)+1):
                if is_palindrome(s[ : i ]):
                    valid.append(s[ : i ])
                    gen_substr(s[ i : ], valid)
                    valid.pop()

        output = []
        gen_substr(s)
        
        return output
       