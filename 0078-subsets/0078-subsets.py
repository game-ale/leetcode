class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def helper(num,ind):
            if ind == len(nums):
                result.append(num[:])
                return 
            helper(num,ind+1)
            num.append(nums[ind])
            helper(num,ind+1)
            if num:
                num.pop()
        helper([],0)
        return result



        