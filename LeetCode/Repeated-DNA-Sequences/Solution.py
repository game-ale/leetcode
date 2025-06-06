class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        t = "AAAAAAAAAAA"
        n = len(s)
        ans = []
        cnt = defaultdict(int)
        if n<=10:
            return ans
        for i in range(n-9):
            cnt[s[i:i+10]]+=1
        for key, val in cnt.items():
            if val>1:
                ans.append(key)
        print(len(t))
        return ans


        
        