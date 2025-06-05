class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = defaultdict(int)
        left = 0
        cnt = 0
        for right in range(len(s)):
            ans[s[right]]+=1
            while left < right and  len(ans) < right-left+1:
                ans[s[left]]-=1
                if ans[s[left]] ==0:
                    del ans[s[left]]
                left +=1
            if len(ans) == right-left+1:
                cnt = max(cnt, right-left+1)
        return cnt

                
        