class Solution:
    def minOperations(self, A: List[int], x: int) -> int:
        k = sum(A) - x
        if k < 0: return -1 
        best = -1
        
        s = i = 0
        
        for j, num in enumerate(A):
            s += num
            while s > k:
                s -= A[i]
                i += 1  
            if s == k:
                best = max(best, j - i + 1)

        return -1 if best < 0 else len(A) - best
