class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def backtraking(i,total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i,total) in dp:
                return dp[(i,total)]
            dp[(i,total)] = backtraking(i + 1 ,total-nums[i]) + backtraking(i + 1 ,total+nums[i])
            return (dp[(i,total)])
        
        return(backtraking(0,0))