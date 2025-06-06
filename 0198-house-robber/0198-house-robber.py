class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        prev2 , prev1 = 0,0
        for num in nums:
            new_rob = max(prev1, prev2 +num)
            prev2 , prev1 = prev1,new_rob

        return prev1
