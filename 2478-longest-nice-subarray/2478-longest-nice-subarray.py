class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        temp , ans , ind = 0,0,0
        for i in range (len(nums)):
            while temp & nums[i]:
                temp ^= nums[ind]
                ind+=1
            ans  = max(i-ind +1, ans)
            temp |=nums[i]
        return ans 

        