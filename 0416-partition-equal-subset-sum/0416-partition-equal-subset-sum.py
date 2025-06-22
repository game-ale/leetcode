class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n  = sum(nums)
        if n%2:
            return False
        target = n//2
        dp = 1
        for num in nums:
            dp|=(dp<<num)
            if dp & (1<<target):
                return True
        return (dp>>target)&1==1
        