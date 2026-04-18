class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = str(n)[::-1]
        return abs(n - int(rev))
        