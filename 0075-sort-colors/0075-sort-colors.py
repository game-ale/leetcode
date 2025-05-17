class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range (1,n):
            j = i-1
            key = nums[i]
            while j>=0 and nums[j]>key:
                nums[j+1]= nums[j]
                j-=1
                nums[j+1] = key
        return nums 

        """
        Do not return anything, modify nums in-place instead.
        """
        