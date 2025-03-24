class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(is_left):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > target or (is_left and nums[mid] == target):
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        left_ind = search(True)
        if left_ind >= len(nums) or nums[left_ind] != target:
            return [-1, -1]
        
        right_ind = search(False) - 1
        return [left_ind, right_ind]
