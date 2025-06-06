class Solution:
    def robotWithString(self, s: str) -> str:
        cnt = Counter(s)
        stk = []
        ans = []
        min_char = "a"
        for char in s:
            stk.append(char)
            cnt[char]-=1
            while min_char !="z" and cnt[min_char]==0:
                min_char = chr(ord(min_char) + 1)
            while stk and stk[-1]<=min_char:
                ans.append(stk.pop())    
        return "".join(ans)



            
            
        
        