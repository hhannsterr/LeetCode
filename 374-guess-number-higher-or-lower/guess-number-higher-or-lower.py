# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def binary_search(num, start, end):
            guessed = guess(num)
            if guessed == 0:
                return num
            elif guessed == -1:
                mid = (start + num) // 2
                return binary_search(mid, start, num)
            else:
                mid = (num + end) // 2
                return binary_search(mid, num, end)
        
        return binary_search(n, 1, 2**31 - 1)
