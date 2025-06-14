class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        t = str(num)
        ind = 0
       
        while ind < len(s) and s[ind] =="9":
            ind+=1
        if ind < len(s):
            s = s.replace(s[ind],"9")
        t= t.replace(t[0],"0")
        return int(s) - int(t)