class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        if t == '':
            return False
        
        s_index = 0
        s_len = len(s)
        for t_letter in t:
            if t_letter == s[s_index]:
                s_index += 1
            if s_index == s_len:
                return True
        
        return False
