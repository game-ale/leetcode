class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        distinct_count = [0] * (len(nums) + 1)
        total_count = 0
        left = 0
        right = 0
        curr_count = 0

        while right < len(nums):
            distinct_count[nums[right]] += 1
            if distinct_count[nums[right]] == 1:
                k -= 1
            if k < 0:
                distinct_count[nums[left]] -= 1
                if distinct_count[nums[left]] == 0:
                    k += 1
                left += 1
                curr_count = 0
            if k == 0:
                while distinct_count[nums[left]] > 1:
                    distinct_count[nums[left]] -= 1
                    left += 1
                    curr_count += 1
                total_count += (curr_count + 1)
            right += 1
        return total_count
