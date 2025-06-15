class Solution:
    def uniquePaths(self, m: int, n: int) -> int:           
        dp = [1] * n
        for col in range(1, m):
            r = [1]
            for row in range(1, n):
                r.append(r[row-1] + dp[row])
            dp = r
        
        return dp[-1]
