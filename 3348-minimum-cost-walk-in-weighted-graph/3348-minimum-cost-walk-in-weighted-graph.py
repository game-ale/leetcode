class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
            self.rank[rootX] += self.rank[rootY]
        else:
            self.parent[rootX] = rootY
            self.rank[rootY] += self.rank[rootX]
        return True


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        weights = [-1] * n
        union_find = UnionFind(n)
        
        for node1, node2, _ in edges:
            union_find.union(node1, node2)
        
        for start, _, weight in edges:
            root = union_find.find(start)
            weights[root] &= weight

        def find_cost(start: int, end: int) -> int:
            if start == end:
                return 0
            root1, root2 = union_find.find(start), union_find.find(end)
            return weights[root1] if root1 == root2 else -1

        return [find_cost(src, dest) for src, dest in query]
