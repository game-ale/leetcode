class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        n = len(nums)
        print(nums)
        for i in range (n-2):
            if nums[i+1]+nums[i+2] > nums[i]:
                return nums[i] + nums[i+1]+nums[i+2]
        return 0

      

        