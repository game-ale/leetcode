class Solution:
    def xorQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        xor = nums[0]
        for i in range(1,n):
            xor^=nums[i]
            nums[i] = xor
        res = []
        for a, b in queries:
            if a>0:
                res.append(nums[a-1]^nums[b])
            else:
                res.append(nums[b])
        return res

        