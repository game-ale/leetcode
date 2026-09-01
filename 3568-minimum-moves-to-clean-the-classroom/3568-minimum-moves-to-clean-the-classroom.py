class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        m = len(classroom)
        n = len(classroom[0])
        id = [[0] * n for _ in range(m)]
        sx = sy = 0
        cnt = 0
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "S":
                    sx, sy = i, j
                elif classroom[i][j] == "L":
                    id[i][j] = 1 << cnt
                    cnt += 1

        full = 1 << cnt
        bestEnergy = [
            [[-1 for _ in range(full)] for _ in range(n)] for _ in range(m)
        ]
        bestEnergy[sx][sy][0] = energy
        Info = collections.deque()
        Info.append((sx, sy, 0, energy, 0))
        while Info:
            x, y, mask, e, steps = Info.popleft()
            if mask == full - 1:
                return steps
            if e == 0:
                continue
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if (
                    nx < 0
                    or nx >= m
                    or ny < 0
                    or ny >= n
                    or classroom[nx][ny] == "X"
                ):
                    continue
                ne = energy if classroom[nx][ny] == "R" else e - 1
                nmask = mask | id[nx][ny]
                if ne > bestEnergy[nx][ny][nmask]:
                    bestEnergy[nx][ny][nmask] = ne
                    Info.append((nx, ny, nmask, ne, steps + 1))
        return -1