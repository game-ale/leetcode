class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def prime(n):
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return 0
            return 1
        p=1
        for i in nums:
            p*=i
        c=0
        for i in range(1,int(p**0.5)+1):
            if p%i!=0:
                continue
            if p//i==i:
                if prime(i):
                    c+=1
            else:
                if prime(p//i):
                    c+=1
                if i!=1 and prime(i):
                    c+=1
        return c