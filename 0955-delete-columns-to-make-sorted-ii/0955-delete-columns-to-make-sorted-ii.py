class Solution:
    def minDeletionSize(self, strs):
        m, n = len(strs), len(strs[0])
        sorted_pairs = [False] * m
        ans = 0

        for col in range(n):
            bad = False

            for row in range(1, m):
                if sorted_pairs[row]:
                    continue
                if strs[row-1][col] > strs[row][col]:
                    bad = True
                    break

            if bad:
                ans += 1
                continue

            for row in range(1, m):
                if (not sorted_pairs[row] and
                    strs[row-1][col] < strs[row][col]):
                    sorted_pairs[row] = True

        return ans