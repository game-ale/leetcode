class Solution:
    def reverseBits(self, n: int) -> int:
        x = bin(n)[2:]
        y = 32-len(x)
        x = "0"*y + x
        x = x[::-1]
        return int(x,2)