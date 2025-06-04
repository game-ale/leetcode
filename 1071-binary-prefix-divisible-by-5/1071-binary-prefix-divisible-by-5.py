class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        total = 0
        temp = []
        i = 0
        n= len(nums)
        ans = []
        while i<n and nums[i]==0:
            ans.append(0)
            i+=1
        for j in range(i,n):
            total = total*2 + nums[j]
            ans.append(total) 
        return [num%5==0 for num in ans]
         
         
        