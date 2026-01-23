class Solution:
    def tribonacci(self, n: int) -> int:
        t0 , t1, t2 = 0,1,1
        if n==0:
            return 0
        if n<=2:
            return 1
        for i in range(3,n+1):
            tem= t2+t1+t0
            t0 , t1, t2  = t1, t2, tem
        return t2
