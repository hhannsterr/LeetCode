class Solution:
    def isUgly(self, n: int) -> bool:
        def divide(num, denom):
            return num // denom, num % denom
        
        if n <= 0:
            return False
        if n == 1:
            return True
        
        whole = n
        while True:
            for denom in [2,3,5]:
                temp, remain = divide(whole, denom)
                if remain == 0:
                    break
            if remain != 0:
                if whole == 1:
                    return True
                else:
                    return False
            whole = temp
