class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        cnt = Counter(s)
        for c in cnt:
            max_len = 0
            if cnt[c]<k:
                for substring in s.split(c):
                    max_len = max(max_len,self.longestSubstring(substring,k))
                return max_len
        return len(s)

                
      