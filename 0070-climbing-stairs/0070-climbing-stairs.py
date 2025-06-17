class Solution:
    def climbStairs(self, n: int) -> int:
        x = 1 
        y = 1
        for i in range(1,n):
            t = y 
            y = y+x
            x = t
        return y
        