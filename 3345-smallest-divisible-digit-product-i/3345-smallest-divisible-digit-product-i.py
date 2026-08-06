class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def func (n):
            prod = 1
            while n:
                x = n%10
                n//=10
                prod*=x
            return prod
        while (func(n)%t):
            n+=1
        return n
        