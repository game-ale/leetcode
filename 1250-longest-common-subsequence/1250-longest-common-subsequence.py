class Solution:
        def longestCommonSubsequence(self, s1: str, s2: str) -> int:
            m = len(s1)
            n = len(s2)
            memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
            for row in range(1, m + 1):
                for col in range(1, n + 1):
                    if s1[row - 1] == s2[col - 1]:
                        memo[row][col] = 1 + memo[row - 1][col - 1]
                    else:
                        memo[row][col] = max(memo[row][col - 1], memo[row - 1][col])
    
            return memo[m][n]