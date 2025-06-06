class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1]*(amount+1)
        dp[0] = 0
        for i in range(1,amount + 1):
            for num in coins:
                if i - num >=0:
                    dp[i] = min(dp[i],1+dp[i-num])
        return dp[amount] if dp[amount]!=amount+1 else -1

        