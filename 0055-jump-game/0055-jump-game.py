class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        flag = n-1
        for i in range (n-1,-1,-1):
            if i + nums[i] >= flag:
                flag = i
        return flag == 0

        