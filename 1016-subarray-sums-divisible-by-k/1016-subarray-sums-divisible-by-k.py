class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem = 0
        ans = 0
        groupmod = defaultdict(int)
        groupmod[0] = 1
        for num in nums:
            rem = (rem + num%k +  k)%k
            ans+=groupmod[rem]
            groupmod[rem]+=1
        return ans


        