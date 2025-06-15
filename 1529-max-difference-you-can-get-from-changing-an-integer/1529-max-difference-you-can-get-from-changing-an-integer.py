class Solution:
    def maxDiff(self, num: int) -> int:
        pos = 0
        s = str(num)
        t = s
        n = len(s)
        i = 0
        j = 0
        while  i< n-1 and s[i]=="9":
            i+=1
        
        s =  s.replace(s[i],"9")
        while  j< n-1 and (t[j]=="1" or t[j]=="0"):
            j+=1
        if j>0 and t[j]!="1":
            t =  t.replace(t[j],"0")
        else:
            t =  t.replace(t[0],"1")
        print(t,s)
        return (int(s)- int(t))