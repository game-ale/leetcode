class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        ans = 1
        mod = 1337
        for e in b[::-1]:
            ans = ans*pow(a,e,mod)%mod
            a = pow(a,10,mod)
        return ans

     
        
        