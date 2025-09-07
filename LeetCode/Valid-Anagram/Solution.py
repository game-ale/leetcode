class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = [c for c in s]
        s.sort()
        t = [c for c in t]
        t.sort()
        if str(s)==str(t):
            return True
        return False