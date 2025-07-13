class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        prefix_sum = 0
        min_diff = float('inf')
        result_index = 0
        
        for i in range(n):
            prefix_sum += nums[i]
            left_avg = prefix_sum // (i + 1)
            
            if i == n - 1:
                right_avg = 0
            else:
                right_avg = (total_sum - prefix_sum) // (n - i - 1)
            
            diff = abs(left_avg - right_avg)
            
            if diff < min_diff:
                min_diff = diff
                result_index = i
        
        return result_index