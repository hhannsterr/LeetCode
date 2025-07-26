class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        front = 0
        end = len(s)-1

        while front < end:
            if s[front] in vowels:
                if s[end] in vowels:
                    temp = s[front]
                    s = s[:front] + s[end] + s[front+1:]
                    s = s[:end] + temp + s[end+1:]
                    front += 1
                end -= 1
            else:
                if s[end] not in vowels:
                    end -= 1
                front += 1
        
        return s
                   