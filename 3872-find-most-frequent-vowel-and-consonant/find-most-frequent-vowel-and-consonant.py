class Solution:
    def maxFreqSum(self, s: str) -> int:
        def max_dict_val(dictionary: dict) -> int:
            return max(dictionary.values())
        
        
        vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        consonants = {
            'b': 0, 'c': 0, 'd': 0, 'f': 0, 'g': 0, 
            'h': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 
            'n': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 
            't': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, 
        }

        for letter in s:
            if letter in vowels:
                vowels[letter] += 1
            else:
                consonants[letter] += 1

        return max_dict_val(vowels) + max_dict_val(consonants)       
