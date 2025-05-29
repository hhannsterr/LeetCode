class Solution:
    def isPalindrome(self, x: int) -> bool:      
        x = str(x)
        reversed_x = x[::-1]
        
        if x == reversed_x:
            return True
        else:
            return False

