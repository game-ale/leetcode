class Solution:
    def hammingWeight(self, n: int) -> int:
        temp = bin(n)
        t = temp.count("1")
        return t