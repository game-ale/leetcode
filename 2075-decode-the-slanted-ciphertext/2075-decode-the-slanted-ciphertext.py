class Solution:
    def decodeCiphertext(self, s: str, m: int) -> str:
        n = len(s)//m
        g = n and [*batched(s,n)] # instead of [*zip(*[iter(s)]*n)]
        return ''.join(g[i][i+j] for j in range(n) for i in range(m) 
            if i+j<n).rstrip()