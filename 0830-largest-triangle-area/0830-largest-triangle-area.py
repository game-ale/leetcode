class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        answer = 0
        for i in range (n-2):
            for j in range(n-1):
                for k in range(n):
                    x1,x2, x3 = points[i][0], points[j][0], points[k][0]
                    y1,y2, y3 = points[i][1], points[j][1],points[k][1]
                    area =  abs (0.5 * ( (x2-x1)*(y3-y1)- (x3-x1)*(y2-y1)))
                    answer = max (answer , area)
        return answer
