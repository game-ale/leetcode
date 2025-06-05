class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        m,n = lcm(q,p)//p,lcm(q,p)//q
        if n%2==0:
            return 2
        elif n%2==1 and m%2==0:
            return 0
        else:
            return 1

        