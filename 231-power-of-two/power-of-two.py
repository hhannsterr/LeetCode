class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def divide_by_two(num):
            return num // 2, num % 2
        
        if n == 0:
            return False
        if n == 1:
            return True

        whole = n
        while True:
            whole, remain = divide_by_two(whole)
            if remain == 1:
                return False
            if whole == 1:
                return True
