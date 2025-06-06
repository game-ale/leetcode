class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        target = s//2
        if s%2!=0:
            return False
        dp = [False]*(target+1)
        dp[0] = True
        for num in nums:
            for i in range (target,num-1,-1):
                dp[i] = dp[i] or dp[i-num]
        return dp[target]
        