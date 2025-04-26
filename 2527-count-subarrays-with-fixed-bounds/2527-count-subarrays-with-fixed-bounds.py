class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        left = 0
        dq_min = deque()
        dq_max = deque()
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                dq_min.clear()
                dq_max.clear()
                left = i + 1
                continue
            while dq_min and nums[dq_min[-1]] >= nums[i]:
                dq_min.pop()
            dq_min.append(i)
            while dq_max and nums[dq_max[-1]] <= nums[i]:
                dq_max.pop()
            dq_max.append(i)
            if nums[dq_min[0]] == minK and nums[dq_max[0]] == maxK:
                start = min(dq_min[0], dq_max[0])
                count += (start - left + 1)
        return count
        