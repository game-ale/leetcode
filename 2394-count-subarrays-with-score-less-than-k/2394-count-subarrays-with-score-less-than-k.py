class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        temp_sum = ans = j = 0
        for i, num  in enumerate(nums):
            temp_sum +=num
            while temp_sum * (i-j+1) >= k:
                temp_sum-=nums[j]
                j+=1
            ans +=(i-j+1)

        return ans 
            
        