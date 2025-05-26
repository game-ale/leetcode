class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk = []
        min_j = float("-inf")
        for num in reversed(nums):

            if num < min_j:
                return True
            while stk and stk[-1]<num:
                min_j = stk.pop()
            stk.append(num)
        return False



        