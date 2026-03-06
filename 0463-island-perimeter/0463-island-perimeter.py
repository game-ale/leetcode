class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        def inbound(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        def dfs(i, j):
            total = 0   
            visited[i][j] = True
            
            for x, y in [[0,-1], [-1,0], [0,1], [1,0]]:
                new_x = x + i
                new_y = y + j

                if not inbound(new_x, new_y) or grid[new_x][new_y] == 0:
                    total += 1
                elif inbound(new_x, new_y) and not visited:
                    total += dfs(new_x, new_y)
                
                
            return total 
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j]  and grid[i][j] == 1:
                    # print("chera")                   
                    total += dfs(i, j)
        return total 
         