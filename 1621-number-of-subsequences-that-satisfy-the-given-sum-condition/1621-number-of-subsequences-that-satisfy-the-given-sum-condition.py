class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cnt = 0
        for mask in range(1,1<<n):
            subset = []
            for i in range(n):
                if (mask>>i)&1==1:
                    subset.append(nums[i])
            less, high = min(subset), max(subset)
            if less + high <=target:
                cnt+=1
        return cnt


        