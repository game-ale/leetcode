class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n  = len(nums)
        while i<n:
            correct_ind = nums[i]-1
            if 0 <= correct_ind < n and nums[i]!= nums[correct_ind]:
                nums[i], nums[correct_ind] = nums[correct_ind], nums[i]
            else:
                i+=1
        for i in range(n):
            if nums[i]!= i+1:
                return i+1
        return i+2


        