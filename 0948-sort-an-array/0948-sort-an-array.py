class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(low, high):
            if low >= high:
                return
            pivot_index = random.randint(low, high)
            nums[high], nums[pivot_index] = nums[pivot_index], nums[high]
            pivot = nums[high]
            greater = high
            i = low
            less = low
            while i <= greater:
                if nums[i] < pivot:
                    nums[less], nums[i] = nums[i], nums[less]
                    less += 1
                    i += 1
                elif nums[i] ==  pivot:
                    i+=1
                else:
                    nums[i], nums[greater] = nums[greater], nums[i]
                    greater -= 1
            quicksort(low, less- 1)
            quicksort(greater + 1, high)

        quicksort(0, len(nums) - 1)
        return nums