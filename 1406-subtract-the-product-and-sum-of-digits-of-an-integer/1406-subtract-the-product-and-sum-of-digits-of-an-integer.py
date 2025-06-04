class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro,add = 1,0
        for c in str(n):
            pro*=int(c)
            add+=int(c)
        return pro - add
        