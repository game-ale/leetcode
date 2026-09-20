class Solution:
    def reverseDegree(self, s: str) -> int:
        value = 0
        for i in range(len(s)):
            temp = 26-ord(s[i]) + ord('a')
            value +=(temp*(i+1))


        return value
