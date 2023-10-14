class Solution:
    def paintWalls(self, cost, time) -> int:
        n = len(cost)
        dp = [[0]*(n+1) for k in range(n+1)]
        for i in range(1, n+1):
            dp[n][i] = float('inf')

        for i in range(n-1,-1,-1):
            for remain in range(1,n+1):
                opt1 = cost[i]+dp[i+1][max(0, remain-1-time[i])]
                opt2 = dp[i+1][remain]
                dp[i][remain] = min(opt1, opt2)
        
        return dp[0][n]