class Solution:
    def minMoves(self, nums: List[int]) -> int:
      
        ma = max(nums)
        ans = 0
        for i in range(len(nums)):
            temp = ma - nums[i]
            ans+=temp
        return ans
