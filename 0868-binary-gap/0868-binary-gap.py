class Solution:
    def binaryGap(self, n: int) -> int:
        bit = bin(n)[2:]
        left, right = bit.index("1"),bit.index("1")+1
        cnt = 1
        ans = 0
        for i in range(right, len(bit)):
            if bit[i]=="1":
                ans  = max(ans,i-left)
                left = i

        return ans
        