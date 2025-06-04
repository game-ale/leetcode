class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x , m = min(nums), max(nums)
        return gcd(x,m)
        