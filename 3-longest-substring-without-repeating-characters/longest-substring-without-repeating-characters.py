class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        start = 0
        hash_map = {}
        for index, letter in enumerate(s):
            if not hash_map.get(letter) or hash_map.get(letter) < start:
                hash_map[letter] = index+1
                longest_length = max(longest_length, index+1 - start)
            else:
                start = hash_map.get(letter)
                hash_map[letter] = index+1
        return longest_length

