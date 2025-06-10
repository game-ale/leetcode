class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sort = sorted(intervals,key = lambda x:x[1])
        n  = len(sort)
        ans = 1
        k = 0
        for i in range(1,len(sort)):
            if sort[k][1]<=sort[i][0]:
                k = i
                ans +=1
        return n-ans

