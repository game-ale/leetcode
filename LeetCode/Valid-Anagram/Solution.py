class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = [char for char in s]
        s.sort()
        t = [char for char in t]
        t.sort()
        if str(s)==str(t):
            return True
        return False
        