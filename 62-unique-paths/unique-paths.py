class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        def countPaths(m, n, dp):
            if m == 0 or n == 0:
                return 1
            if dp[m][n]:
                return dp[m][n]
        
            dp[m][n] = countPaths(m - 1, n, dp) + countPaths(m, n - 1, dp)
            return dp[m][n]
        
        return countPaths(m - 1, n - 1, dp)
    
        
        