class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def com(ind: int, target: int, ds: List[int]):
            if ind == len(candidates) or target < 0:
                if target == 0:
                    ans.append(ds.copy())
                return
            
            if candidates[ind] <= target:
                ds.append(candidates[ind])
                com(ind, target - candidates[ind], ds)
                ds.pop()
            
            com(ind + 1, target, ds)
        
        ans = []
        com(0, target, [])
        return ans