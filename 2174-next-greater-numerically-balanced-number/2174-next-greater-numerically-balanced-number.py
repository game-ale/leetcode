class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range (n+1,1224445):
            cnt = Counter(str(i))
            if all( cnt[key]== int(key) for key in cnt):
                return i
        