class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        x = max (nums)
        for num in nums:
            x = gcd(x,num)
        return True if x==1 else False
        