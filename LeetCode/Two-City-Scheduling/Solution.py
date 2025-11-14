class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans = 0
        costs.sort(key = lambda x:x[0]-x[1])
        i = 0
        n = len(costs)
        while i<n//2:
            ans+=(costs[i][0]+costs[-(i+1)][1])
            i+=1
        return ans
            

        