class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = nums[0]
        n = len(nums)
        dp = [0]*(n)
        if len(nums)<=2:
            return max(nums)
        dp[0], dp[1] = nums[0],nums[1]
        mval = nums[0]
        for i in range (2,n):
            dp[i] = max(dp[i-1], mval + nums[i])
            ans = max(dp[i],ans)
            mval = max(mval, dp[i-1])
        return ans

        