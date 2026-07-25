class Solution:
    def maxProduct(self, n: int) -> int:
        ans = []
        while n:
            dig = n%10
            n//=10
            ans.append(dig)
        ans.sort()
        return ans[-1]*ans[-2]


