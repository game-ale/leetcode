class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)-1
        ans = 0
        for i in range(1,n):
            if nums[i-1] + nums[i+1] == nums[i]//2 and nums[i]%2 == 0:
                ans += 1
        return ans 