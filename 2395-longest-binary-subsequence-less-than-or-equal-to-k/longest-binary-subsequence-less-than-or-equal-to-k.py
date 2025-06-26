class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        binary_k = int(bin(k)[2:])
        while True:
            if int(s) > binary_k:
                s = s.replace('1', '', 1)
            else:
                return len(s)
