class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n, m = len(nums), len(set(nums))
        cnt = defaultdict(int)
        left = 0
        ans = 0
        
        for right in range(n):
            cnt[nums[right]] += 1
            
            while len(cnt) == m:
                ans += n - right  
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
                
        return ans

            

        