class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        uf = list(range(m * n))
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf[find(x)] = find(y)

        for i, row in enumerate(grid):
            for j, street in enumerate(row):
                # union right if on street 1, 4, 6
                # and right neighbor is on 1, 3, 5
                idx = i * n + j
                if street in (1,4,6) and j < n - 1 and grid[i][j+1] in (1,3,5):
                    union(idx + 1, idx)
                # union down if on street 2, 3, 4
                # and down neighbor is on 2, 5, 6
                if street in (2,3,4) and i < m - 1 and grid[i+1][j] in (2,5,6):
                    union(idx + n, idx)

        return find(0) == find(m * n - 1)