class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stk = []
        ans = 0
        for num in nums:
            while stk and stk[-1]>num:
                stk.pop()
            if num == 0:
                continue
            if not stk or stk[-1]<num:
                ans +=1
                stk.append(num)
        return ans
        