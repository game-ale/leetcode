class Solution:
    def minimumDeleteSum(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = ord(s1[i]) + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        total = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        return total - 2 * dp[0][0]
