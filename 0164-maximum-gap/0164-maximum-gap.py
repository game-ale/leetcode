class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        max_num = max(nums) 
        n = len(nums)
        exp = 1
        def radixsort():
            cnt = [0]*10
            result = [0]*n
            for i in range(n):
                ind = (nums[i]//exp)%10
                cnt[ind]+=1
            for i in range(1,10):
                cnt[i]+= cnt[i-1]     
            for i in range(n-1,-1, -1):
                ind =cnt[(nums[i]//exp)%10] 
                result[ind-1] = nums[i]
                cnt[(nums[i]//exp)%10]-=1
            for i in range (n):
                nums[i] = result[i]       
        while max_num//exp > 0:
            radixsort()
            exp*=10
        ans = 0
        for i in range(1,n):
            ans = max(ans,nums[i]- nums[i-1])
        return ans


        