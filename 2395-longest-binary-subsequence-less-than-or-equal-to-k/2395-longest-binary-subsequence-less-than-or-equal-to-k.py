class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans = format(k,'b')
        dis = len(ans)
        one  = s[:-dis].count("1")
        temp = s[-dis:]
        res = len(s)-one
        return res if int(temp,2)<=k else res -1
        