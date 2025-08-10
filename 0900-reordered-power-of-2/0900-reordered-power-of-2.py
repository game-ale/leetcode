class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        cnt = Counter(str(n))
        for i in range(31):
            x = pow(2,i)
            cnt1 = Counter(str(x))
            if cnt1 ==cnt:
                return True
        return False
        