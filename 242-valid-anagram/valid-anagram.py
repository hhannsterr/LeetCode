class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_hash_map(string):
            hash_map = {}
            for letter in string:
                if letter in hash_map:
                    hash_map[letter] += 1
                else:
                    hash_map[letter] = 1
            return hash_map


        if len(s) > len(t):
            hash_map_first = get_hash_map(s)
            hash_map_second = get_hash_map(t)
        else:
            hash_map_first = get_hash_map(t)
            hash_map_second = get_hash_map(s)

        for k, v in hash_map_first.items():
            if k not in hash_map_second:
                return False
            if hash_map_second[k] != v:
                return False
        return True
