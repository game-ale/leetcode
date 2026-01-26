class Solution:
    def minimumAbsDifference(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 1
        n = len(nums)
        diff = nums[1]-nums[0]
        ans = [[nums[0],nums[1]]]
        while i<n-1:
            if nums[i+1]-nums[i]==diff:
                ans.append([nums[i],nums[i+1]])
            elif nums[i+1]-nums[i]<diff:
                diff = nums[i+1]-nums[i]
                ans = []
                ans.append([nums[i],nums[i+1]])
            i+=1
        return ans 

            
        

        