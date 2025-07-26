class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        def gen_hash_map(string):
            hash_map = {}
            hash_set = set()
            for letter in string:
                if letter in hash_map:
                    hash_map[letter] += 1
                else:
                    hash_map[letter] = 1
                    hash_set.add(letter)
            return hash_map, hash_set

        
        s_map, s_set = gen_hash_map(s)
        t_map, t_set = gen_hash_map(t)

        if len(s_set) != len(t_set):
            return (t_set - s_set).pop()
        
        for s_key, s_val in s_map.items():
            if s_val != t_map[s_key]:
                return s_key
