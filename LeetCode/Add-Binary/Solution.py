class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = format((int(a,2) + int(b,2)),'b')
        return c

        