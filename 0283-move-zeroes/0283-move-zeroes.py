class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left, right = 0 , 0
        n = len(nums)
       
        while right < n:
            if nums[right]!=0:
                nums[left], nums[right] = nums[right],nums[left]
                left+=1
            right+=1
        return nums

            

        """
        Do not return anything, modify nums in-place instead.
        """
        