class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        ans = 0
        mod = 10**9 + 7
        for num in nums:
            cnt[num - int(str(num)[::-1])]+=1
        for _, val in cnt.items():
            ans+=(val*(val-1)//2)
        return ans%mod
