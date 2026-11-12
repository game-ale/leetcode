class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        max_length = 0

        # Find longest strictly increasing subarray
        for start in range(len(nums)):
            curr_length = 1
            for pos in range(start + 1, len(nums)):
                # Extend subarray if next element is larger
                if nums[pos] > nums[pos - 1]:
                    curr_length += 1
                else:
                    # Break if sequence is not increasing anymore
                    break
            max_length = max(max_length, curr_length)

        # Find longest strictly decreasing subarray
        for start in range(len(nums)):
            curr_length = 1
            for pos in range(start + 1, len(nums)):
                # Extend subarray if next element is smaller
                if nums[pos] < nums[pos - 1]:
                    curr_length += 1
                else:
                    # Break if sequence is not decreasing anymore
                    break
            max_length = max(max_length, curr_length)

        return max_length  # Return the longer of increasing or decreasing sequences