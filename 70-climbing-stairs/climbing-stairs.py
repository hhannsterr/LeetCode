class Solution:
    def climbStairs(self, n: int) -> int:        
        if n < 3:
            return n
        store = [1, 2]
        for i in range(3, n+1):
            store[0], store[1] = store[1], store[0] + store[1]
        return store[1]
