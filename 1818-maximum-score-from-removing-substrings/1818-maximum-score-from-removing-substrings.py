class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        tem = 'ab' if x> y else 'ba'
        tem1 = 'ba'if x>y else 'ab'
        a, b = 0,0
        stk = []
        for i in range(len(s)):
            if stk and "".join([stk[-1],s[i]]) == tem:
                stk.pop() 
                a+=1
                continue
            stk.append(s[i])
        stk1 = []
        for i in range(len(stk)):
            if stk1 and "".join([stk1[-1],stk[i]]) == tem1:
                stk1.pop() 
                b+=1
                continue
            stk1.append(stk[i])
        total = a*max(x,y) + b*min(x,y)
        return total
        
        