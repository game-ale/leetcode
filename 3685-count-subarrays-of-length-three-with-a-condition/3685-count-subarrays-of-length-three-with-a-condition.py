class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        return sum (1 for i in range(1, len(nums)-1) if nums[i-1] + nums[ i+1] == nums[i]//2 and nums[i]%2==0)