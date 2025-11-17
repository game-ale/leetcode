class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        ind1  = -1
        if 1 in nums:
            ind1 = nums.index(1) 
        for i in range(ind1 + 1, len(nums)):
            if nums[i]==1:
                if (i - ind1 - 1)<k:
                    return False
                else:
                    ind1 = i
        return True
        