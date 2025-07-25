class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(p)
        n = len(p)
        cnts = Counter(s[:n])
        ans = []
        if cnt ==cnts:
            ans.append(0)
        cnts[s[0]]-=1
        for i in range(n,len(s)):
            cnts[s[i]]+=1
            if cnt==cnts:
                ans.append(i-n+1)
            cnts[s[i-n+1]]-=1
        return ans
            


        