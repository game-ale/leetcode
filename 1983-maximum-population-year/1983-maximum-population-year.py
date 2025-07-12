class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        pre = [0]*101
        for a,b in logs:
            pre[a-1950]+=1
            pre[b-1950]-=1
        pre = list(accumulate(pre))
        val = max(pre)
        
        return (pre.index(val)+1950)
      