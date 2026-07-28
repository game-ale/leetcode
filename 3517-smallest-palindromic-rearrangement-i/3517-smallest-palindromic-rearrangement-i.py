class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = Counter( s)
        odd  = ''
        unique = []
        ans = ""
        for key, val in cnt.items():
            if val%2:
                odd = key
            unique.append(key)
        unique.sort()
        for st in unique:
            ans = ans + ((cnt[st]//2)*st)
        answer = ans + odd + ans[::-1]
        return answer 
        