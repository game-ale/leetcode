class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = Counter(x%value for x in nums)
        mex = 0
        while cnt[mex%value] >0:
            cnt[mex%value]-=1
            mex+=1
            
            
        return mex
        