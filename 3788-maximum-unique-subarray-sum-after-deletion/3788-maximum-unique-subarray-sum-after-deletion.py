class Solution:
    def maxSum(self, nums: List[int]) -> int:
        st = list(set(nums))
        st.sort()
        if st[-1]<0:
            return st[-1]
        else:
            return sum(num for num in st if num > 0)
