class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            l = 1
            for x in nums[i:]:
                l = lcm(l,x)
                ans+=l==k
                if l>k:
                    break
        return ans
