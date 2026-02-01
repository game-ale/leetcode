class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = sum(nums[:3])
        for i in range(1, len(nums)-1):
            for j in range(i+1, len(nums)):
                temp  = nums[0] + nums[i] + nums[j]
                ans = min (ans, temp)
        return ans


        