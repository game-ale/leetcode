class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        range_ = max(nums) - min(nums)
        if len(nums)<2:
            return 0

        x= min(nums)
        ans = 0
        bsize = range_ //(len(nums)-1) or 1
        num_buck = range_//bsize + 1
        hash_ = [[] for i in range (num_buck)]
        for num in  nums:
            hash_[(num-x)//bsize].append(num)
        for i in range(num_buck):
            hash_[i].sort()
        k  = 0
        for i in range(num_buck):
            for j in range(len(hash_[i])):
                nums[k] = hash_[i][j]
                k+=1
        
        for i in range(1,len(nums)):
            ans = max(ans,nums[i]-nums[i-1])
        return ans
        



                
    
            

    


        