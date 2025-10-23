class Solution:
    def hasSameDigits(self, s: str) -> bool:
        rep = list(s)
        while len(rep)>2:
            n = len(rep)
            for  i in range(n-1):
                rep[i] = str((int(rep[i])+ int(rep[i+1]))%10)
            rep.pop()
        return rep[0]==rep[1]
        