class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        ans = 0
        cnt = defaultdict(int)
        for right in range(len(fruits)):
            cnt[fruits[right]] += 1

            while len(cnt) > 2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    del cnt[fruits[left]]
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans



            


        