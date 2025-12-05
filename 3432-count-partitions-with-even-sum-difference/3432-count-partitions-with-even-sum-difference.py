class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        right,left,ans = sum(nums) , 0,0
        for i in range(len(nums)-1):
            left+=nums[i]
            right-=nums[i]
            if abs(left-right)%2==0:
                ans+=1
        return ans

        