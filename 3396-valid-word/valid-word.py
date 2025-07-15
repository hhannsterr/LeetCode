class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        if not word.isalnum():
            return False
        
        vowel_done = False
        conso_done = False
        
        vowel = set('aeiouAEIOU')
        conso = set('bcdfghjklmnpqrstwxyzBCDFGHJKLMNPQRSTVWXYZ')

        index = -1
        for i in range(len(word)):
            if word[i] in vowel:
                vowel_done = True
                index = i
                break
            if word[i] in conso:
                conso_done = True
                index = i
                break

        if index == -1:
            return False

        if vowel_done:
            for letter in word[i:]:
                if letter in conso:
                    return True
        
        if conso_done:
            for letter in word[i:]:
                if letter in vowel:
                    return True
        
        return False
