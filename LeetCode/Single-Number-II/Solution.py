class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = 0
        two = 0
        for num in nums:
            one = (one^num)&~two
            two = (two ^num)&~one
        return one
