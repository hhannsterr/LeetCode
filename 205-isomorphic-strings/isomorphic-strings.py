class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map_s = {}
        hash_map_t = {}
        for s_letter, t_letter in zip(s, t):
            if s_letter in hash_map_s:
                if hash_map_s[s_letter] != t_letter:
                    return False
            else:
                hash_map_s[s_letter] = t_letter

            if t_letter in hash_map_t:
                if hash_map_t[t_letter] != s_letter:
                    return False
            else:
                hash_map_t[t_letter] = s_letter
        
        return True
