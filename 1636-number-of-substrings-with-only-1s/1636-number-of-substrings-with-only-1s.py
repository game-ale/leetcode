class Solution:
    def numSub(self, s: str) -> int:
        total, consecutive = 0, 0
        length = len(s)
        for i in range(length):
            if s[i] == "0":
                total += consecutive * (consecutive + 1) // 2
                consecutive = 0
            else:
                consecutive += 1

        total += consecutive * (consecutive + 1) // 2
        total %= 10**9 + 7
        return total