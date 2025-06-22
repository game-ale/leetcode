class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        rem = n%k
        div = n//k
        i = 0
        ans = []
        for _ in range(div):
            ans.append(s[i:i+k])
            i+=k
        if rem:
            temp = s[-rem:]+fill*(k-rem)
            ans.append(temp)
        return ans



        