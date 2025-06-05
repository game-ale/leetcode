class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ans = []
        for i in range(1,int(n**0.5)+1):
            if i*i != n:
                if n%i==0:
                    ans.append(i)
                    ans.append(n//i)
            if i*i == n and n%i ==0:
                ans.append(i)
        ans.sort()
        print(ans, k)
        return ans[k-1] if k<=len(ans) else -1
