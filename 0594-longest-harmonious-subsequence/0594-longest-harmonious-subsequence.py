class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        ans,left = 0,0
        for right in range(len(nums)):
            if nums[right] - nums[left]==1:
                ans = max(ans , right - left + 1)
            while nums[right] - nums[left] >1:
                left+=1
        return ans

        