class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        n = min(n, 10)
        
        tot = 10  
        un = 9
        a = 9
        
        for i in range(2, n + 1):
            un *= a
            tot += un
            a -= 1
        
        return tot
        

        