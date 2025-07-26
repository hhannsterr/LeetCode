class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def get_hash_map(string):
            hash_map = {}
            for letter in string:
                if letter in hash_map:
                    hash_map[letter] += 1
                else:
                    hash_map[letter] = 1
            return hash_map

        
        if ransomNote in magazine:
            return True
        
        hash_map_note = get_hash_map(ransomNote)
        hash_map_maga = get_hash_map(magazine)

        for letter, amount in hash_map_note.items():
            if letter not in hash_map_maga:
                return False
            else:
                if amount > hash_map_maga[letter]:
                    return False

        return True
