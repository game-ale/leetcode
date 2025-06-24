class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pair = [weights[i] + weights[i + 1] for i in range(n - 1)]
        
        pair.sort()
        ans = 0
        for i in range(k - 1):
            ans += pair[n - 2 - i] - pair[i]
        return ans