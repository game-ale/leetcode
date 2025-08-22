class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        elif n<0:
            return 1/self.myPow(x,-n)
        elif n%2==1:
            half = self.myPow(x,(n-1)//2)
            return half * half * x
        else:
            half = self.myPow(x,n//2)
            return half*half