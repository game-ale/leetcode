class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            temp = nums[i]%3
            min_take = min ( 3-temp , temp)
            ans+=min_take
        return ans
        