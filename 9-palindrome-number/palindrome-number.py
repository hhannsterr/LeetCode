class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        x = str(x)
        reversed_x = x[::-1]
        
        return x == reversed_x

