class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, columns = len(mat), len(mat[0])
        dist = [[float('inf')] * columns for _ in range(rows)]
        queue = deque()
        for r in range(rows):
            for c in range(columns):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < columns and dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
        return dist