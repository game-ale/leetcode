class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        tot = 0
        for row in grid:
            ans = sum(row)
            tot+=ans
        if tot%2:
            return False
        temp = 0
        for row in grid:
            rw = sum(row)
            temp+=rw
            if temp==tot-temp:
                return True
        n, m = len(grid), len(grid[0])
        temp = 0
        for i in range(m):
            cl = 0
            for j in range(n):
                cl+=grid[j][i]
            temp+=cl
            if temp == tot-temp:
                return True
        return False
            

        
        
        