class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        return bisect_right(list(accumulate(sorted(costs))), coins)