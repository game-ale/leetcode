def longestSubarray(self, nums: List[int], limit: int) -> int:
    max_deque = deque()
    min_deque = deque()
    left = 0

    for right in range(len(nums)):
        # Maintain the max_deque in decreasing order
        while max_deque and max_deque[-1] < nums[right]:
            max_deque.pop()
        max_deque.append(nums[right])

        # Maintain the min_deque in increasing order
        while min_deque and min_deque[-1] > nums[right]:
            min_deque.pop()
        min_deque.append(nums[right])

        # Check if the current window exceeds the limit
        if max_deque[0] - min_deque[0] > limit:
            # Remove the elements that are out of the current window
            if max_deque[0] == nums[left]:
                max_deque.popleft()
            if min_deque[0] == nums[left]:
                min_deque.popleft()
            left += 1 # increase the left as well if the interval is invalid
    return len(nums)-left