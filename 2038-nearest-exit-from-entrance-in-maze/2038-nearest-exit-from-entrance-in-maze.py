class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dirc = [(-1,0),(1,0),(0,1),(0,-1)]
        que = deque([(entrance[0],entrance[1],0)])
        n,m = len(maze),len(maze[0])
        maze[entrance[0]][entrance[1]] = "+"
        while que:
            x,y,step = que.popleft()
            if ((x==0 or x==n-1 or y==0 or y==m-1)and [x,y]!=entrance):
                return step
            for dx, dy in dirc:
                nx, ny = x + dx, y + dy 
                if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '.':
                    maze[nx][ny] = '+'  
                    que.append((nx, ny, step + 1))
        return -1
                
        