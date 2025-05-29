class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        output = ''
        for letter in strs[0]: 
            for word in strs:
                if len(word) <= i:
                    return output
                if word[i] != letter:
                    return output
            output += letter
            i += 1
        return output
