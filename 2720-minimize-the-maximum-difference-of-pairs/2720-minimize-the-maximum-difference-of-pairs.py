class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        def pairs(max_diff):
            count = 0
            i = 1
            while i < len(nums):
                if nums[i] - nums[i - 1] <= max_diff:
                    count += 1
                    i += 2  
                else:
                    i += 1  
            return count >= p
        
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if pairs(mid):
                right = mid
            else:
                left = mid + 1
        return left




        