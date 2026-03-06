class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        i = 0
        while i < n and s[i]=="1":
            i+=1
        return s.count("1")==i
        