class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        ans = [0]*(n)
        for a,b in queries:
            ans[a]+=1
            if b<n-1:
                ans[b+1]-=1
        for i in range(1,n):
            ans[i]+=ans[i-1]
        for i in range(n):
            if ans[i]<nums[i]:
                return False
        return True

        