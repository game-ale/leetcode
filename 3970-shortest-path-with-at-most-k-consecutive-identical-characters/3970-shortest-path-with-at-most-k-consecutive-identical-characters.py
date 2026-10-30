class Solution:
    def shortestPath(
        self, n: int, edges: List[List[int]], labels: str, k: int
    ) -> int:
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))

        dis = [[2**31 - 1] * (k + 1) for _ in range(n)]
        # {shortest path length, node index, number of consecutive identical letters at the end}
        pq = []

        dis[0][1] = 0
        heappush(pq, (0, 0, 1))

        while pq:
            d, x, cnt = heappop(pq)

            if d > dis[x][cnt]:
                continue
            if x == n - 1:
                return d

            for y, w in g[x]:
                new_cnt = cnt + 1 if labels[x] == labels[y] else 1
                if new_cnt > k:
                    continue

                nd = d + w
                if nd < dis[y][new_cnt]:
                    dis[y][new_cnt] = nd
                    heappush(pq, (nd, y, new_cnt))

        return -1