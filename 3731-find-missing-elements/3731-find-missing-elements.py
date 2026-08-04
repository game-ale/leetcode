class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        x_min = nums[0]
        y_max = nums[-1]
        ans = []
        nums = set(nums)
        for i in range (x_min , y_max):
            if i not in nums:
                ans.append(i)
        return ans 
