class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''
        for letter in s:
            if letter.isalpha() or letter.isdigit():
                temp += letter.lower()
        print(temp, temp[::-1])
        return temp == temp[::-1]