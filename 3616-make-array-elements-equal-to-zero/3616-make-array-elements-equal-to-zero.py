class Solution:
    def countValidSelections(self, nums):
        count = 0
        nonZeros = sum(1 for x in nums if x > 0)
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                if self.isValid(nums, nonZeros, i, -1):
                    count += 1
                if self.isValid(nums, nonZeros, i, 1):
                    count += 1
        return count

    def isValid(self, nums, nonZeros, start, direction):
        temp = nums[:]
        curr = start
        while nonZeros > 0 and 0 <= curr < len(nums):
            if temp[curr] > 0:
                temp[curr] -= 1
                direction *= -1
                if temp[curr] == 0:
                    nonZeros -= 1
            curr += direction
        return nonZeros == 0