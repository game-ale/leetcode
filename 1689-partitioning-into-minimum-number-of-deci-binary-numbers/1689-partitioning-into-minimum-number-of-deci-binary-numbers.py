class Solution:
    def minPartitions(self, n: str) -> int:
        return ord(max(x for x in n))-ord('0')