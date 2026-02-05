class Solution:
    def constructTransformedArray(self, nums):
        n = len(nums)
        return [nums[((i + nums[i]) % n + n) % n] for i in range(n)]