class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[[0] * 3 for _ in range(k + 1)] for _ in range(n)]

        # initialize the state on day 0
        for j in range(1, k + 1):
            dp[0][j][1] = -prices[0]
            dp[0][j][2] = prices[0]

        for i in range(1, n):
            for j in range(1, k + 1):
                dp[i][j][0] = max(
                    dp[i - 1][j][0],
                    max(
                        dp[i - 1][j][1] + prices[i], dp[i - 1][j][2] - prices[i]
                    ),
                )
                dp[i][j][1] = max(
                    dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i]
                )
                dp[i][j][2] = max(
                    dp[i - 1][j][2], dp[i - 1][j - 1][0] + prices[i]
                )

        return dp[n - 1][k][0]