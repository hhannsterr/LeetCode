class Solution:
    def possibleStringCount(self, word: str) -> int:
        output = 0
        hash_map = {'initial': 1}
        for letter in word:
            if letter in hash_map:
                hash_map[letter] += 1
            else:
                output += hash_map.popitem()[1]
                hash_map[letter] = 0

        return output + hash_map.popitem()[1]
