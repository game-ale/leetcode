class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        for num in nums:
            if not ans or num>ans[-1]:
                ans.append(num)
            else:
                ind = bisect_left(ans,num)
                ans[ind] = num
        return len(ans)
            