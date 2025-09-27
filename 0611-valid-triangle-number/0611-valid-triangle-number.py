class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range (n):
            for j in range (i+1,n-1):
                target = nums[i]+nums[j]-1
                ind = bisect_right(nums,target)
                if ind >j:
                    ans+=(ind-j-1)
               

        return ans


        


        