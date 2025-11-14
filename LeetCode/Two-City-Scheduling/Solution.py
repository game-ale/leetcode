class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:x[0]-x[1])
        ans = 0
        i, n = 0,len(costs)
        while i<n//2:
            ans+=(costs[i][0] +costs[-(i+1)][1])
            i+=1

        
        return ans

        