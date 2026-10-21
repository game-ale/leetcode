class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        mx, mn = max(s), min(s)
        if all(a <= b for a, b in zip(s, s[1:])):
            return 0
        if n == 2:
            return -1
        if s[0] == mn or s[-1] == mx:
            return 1
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2
        return 3