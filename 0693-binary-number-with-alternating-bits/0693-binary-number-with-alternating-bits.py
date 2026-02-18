class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = bin(n)[2:]
        for i in range(1,len(x)):
            if x[i]==x[i-1]:
                return False
        return True
        