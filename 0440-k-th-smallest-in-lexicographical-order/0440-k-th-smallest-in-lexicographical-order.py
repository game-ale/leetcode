class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1

        while k > 0:
            steps = self._count(n, curr, curr + 1)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1

        return curr

    def _count(self, n, a, b):
        res = 0
        while a <= n:
            res += min(n + 1, b) - a
            a *= 10
            b *= 10
        return res
