from collections import defaultdict
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = defaultdict(int)
        for w in words:
            count[w] += 1
        
        ans = 0
        used_middle = False
        
        for w in list(count.keys()):
            rev = w[::-1]
            if w == rev:  
                
                pairs = count[w] // 2
                ans += pairs * 4  
                if not used_middle and count[w] % 2 == 1:
                    ans += 2
                    used_middle = True
                count[w] = 0  
            else:
                if w < rev: 
                    pairs = min(count[w], count[rev])
                    ans += pairs * 4
                    count[w] -= pairs
                    count[rev] -= pairs
        
        return ans
