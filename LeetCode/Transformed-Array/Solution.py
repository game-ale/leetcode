class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i, x in enumerate(nums):
            result.append(nums[(i+n+x)%n] if x else 0 )
        return result
    