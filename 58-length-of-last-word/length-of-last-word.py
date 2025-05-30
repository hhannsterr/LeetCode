class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        first_spacebar = True
        count = 0
        for letter in s[::-1]:
            if first_spacebar:
                if letter != ' ':
                    count += 1
                    first_spacebar = False
            else:
                if letter != ' ':
                    count += 1
                else:
                    break
        return count
