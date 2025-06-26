class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        def remove_one(s, index):
            return s[:index] + s[index + 1:]
        
        ones = []
        count = 0
        for index, letter in enumerate(s):
            if letter == '1':
                ones.append(index-count)
                count += 1
        ones = ones[::-1]

        binary_k = int(bin(k)[2:])
        while True:
            if int(s) > binary_k:
                s = remove_one(s, ones.pop())
            else:
                return len(s)
