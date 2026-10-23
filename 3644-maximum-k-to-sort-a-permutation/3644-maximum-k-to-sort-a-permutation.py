class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1
        for i in range(n):
            if nums[i] == i:
                continue
            res &= nums[i]
        return 0 if res == -1 else res