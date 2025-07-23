class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        n = len(nums)
        ans = 0
        cnt = 1 
        if n<=1:
            return n
        for i in range(1,n):
            if nums[i]-nums[i-1]==1:
                cnt+=1
            else:
                cnt = 1
            ans = max(ans,cnt)
        return ans

        