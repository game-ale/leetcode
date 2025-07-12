class Solution:
    def reverseBits(self, n: int) -> int:
        k = bin(n)[2:].zfill(32)
        k = k[::-1]
        return (int(k,2))
        