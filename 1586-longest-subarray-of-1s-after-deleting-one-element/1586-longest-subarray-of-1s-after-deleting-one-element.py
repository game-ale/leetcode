class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        maxlen = 0
        cnt =0
        n = len(nums)
        for right in range (n):
            if nums[right]==0:
                cnt+=1
            while cnt>1:
                if nums[left]==0:
                    cnt-=1
                left+=1
            maxlen = max(maxlen,right-left)
        if maxlen == n:
            maxlen = n-1
        return maxlen
            