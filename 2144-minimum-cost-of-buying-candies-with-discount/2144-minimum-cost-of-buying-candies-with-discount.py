class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        cost.reverse()
        total = sum(cost)
        min_sum = 0
        for i in range(2,len(cost),3):
            min_sum+=cost[i]
        return total-min_sum




