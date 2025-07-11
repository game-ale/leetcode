class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left<= right:
            mid = (left + right)//2
            ans = 0 
            for num in nums:
                ans+=ceil(num/mid)
            if ans > threshold:
                left = mid+1
            else:
                right = mid - 1
        return left
        