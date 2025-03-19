class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        for i in range (len(nums)-2):
            if nums[i] == 1:
                continue
            else:
                cnt+=1
                for k in range (i,i+3):
                    if nums [k]==0:
                        nums[k]=1
                    else:
                        nums[k]=0
        if all(x == 1 for x in nums):
            return cnt
        else:
            return -1