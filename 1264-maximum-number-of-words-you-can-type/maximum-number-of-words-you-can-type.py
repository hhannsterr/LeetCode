class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(' ')
        count = 0
        for word in words:
            not_exist = True
            for letter in brokenLetters:
                if letter in word:
                    not_exist = False
                    break
            if not_exist:
                count += 1
        
        return count
        