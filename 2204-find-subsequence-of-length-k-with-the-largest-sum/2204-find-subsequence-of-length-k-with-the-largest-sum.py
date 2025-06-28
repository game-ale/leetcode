class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        temp = sorted(nums,reverse = True)[:k]
        cnt = Counter(temp)
        ans = []
        for num in nums:
            if cnt[num]:
                ans.append(num)
                cnt[num]-=1
        return ans
        