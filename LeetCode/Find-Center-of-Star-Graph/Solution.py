class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        cnt = defaultdict(int)  
        for a,b in edges:
            cnt[a]+=1
            cnt[b]+=1
        cnt = sorted(cnt.keys(), key=lambda x: cnt[x],reverse =True)
       
        return cnt[0]

       
        