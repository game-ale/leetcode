class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0,1,1]
        if n<2:
            return n
        if n == 2:
            return 1
        for i in range(3,n+1):
            ans = dp[0] + dp[1] + dp[2] 
            dp[0] , dp[1] , dp[2]  = dp[1],dp[2],ans 
        return dp[2]
