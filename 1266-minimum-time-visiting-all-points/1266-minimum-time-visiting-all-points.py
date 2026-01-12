class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points) - 1):
            x, y = points[i]
            new_x,new_y = points[i + 1]
            ans += max(abs(new_x - x), abs(new_y - y))
        
        return ans