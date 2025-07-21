class Solution:
    def makeFancyString(self, s: str) -> str:
        def delete(string, start, end):
            return string[:start] + string[end:]

        count = 1
        temp = s[0]
        fancy = temp
        for letter in s[1:]:
            if letter == temp:
                if count < 2:
                    count += 1
                    fancy += letter
            else:
                temp = letter
                count = 1
                fancy += letter

        return fancy
