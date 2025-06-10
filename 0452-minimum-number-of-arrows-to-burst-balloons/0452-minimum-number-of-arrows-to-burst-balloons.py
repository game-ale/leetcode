class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 0
        sort = sorted(points,key = lambda x:x[1])
        n  = len(sort)
        ans = 1
        k = 0
        print(sort)

        x = sort[0][1]
        for i in range(1,len(sort)):
            x = min(x,sort[i-1][1])
            if x <sort[i][0]:
                x = sort[i][1]
                ans +=1
        return ans
        