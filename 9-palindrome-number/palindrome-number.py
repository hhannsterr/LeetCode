class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        x = str(x)
        end = int(len(x)/2)
        
        for i in range(end):
            if x[i] != x[-i-1]:
                return False
        return True

