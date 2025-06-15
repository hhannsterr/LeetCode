class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = obstacleGrid[0].copy()
        check = True
        for i in range(n):
            if dp[i] == 0 and check:
                dp[i] = 1
            elif dp[i] == 1:
                dp[i] = 0
                check = False

        print(dp)
        for row in range(1, m):
            r = [dp[0]] if obstacleGrid[row][0] == 0 else [0]
            for col in range(1, n):
                if obstacleGrid[row][col] == 0:
                    r.append(r[col-1] + dp[col])
                else:
                    r.append(0)
            print(r)
            dp = r
        
        return dp[-1]
