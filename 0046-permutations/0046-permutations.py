class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs (ind):
            if ind == len(nums):
                ans.append(nums[:])
                return 
            for i in range(ind, len(nums)):
                nums[ind],nums[i] = nums[i],nums[ind]
                dfs(ind + 1)
                nums[ind],nums[i] = nums[i],nums[ind]
        ans = []
        dfs(0)
        return ans
        