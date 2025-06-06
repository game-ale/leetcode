class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=1:
            return n
        if n ==2:
            return 1
        prev1,prev2 , prev3 = 0,1,1
        for i in range(3,n+1):
            new = prev1 + prev2 + prev3
            prev1,prev2 , prev3 = prev2, prev3 , new
            print(prev1,prev2,prev3)
        return prev3

        