class Solution:
    def maxDifference(self, s: str) -> int:
        hash_map = {}
        for letter in s:
            if hash_map.get(letter):
                hash_map[letter] += 1
            else:
                hash_map[letter] = 1
        
        max_odd = -1000000
        min_even = 1000000
        for _, value in hash_map.items():
            if value % 2 == 0:
                min_even = min(min_even, value)
            else:
                max_odd = max(max_odd, value)

        return max_odd - min_even
