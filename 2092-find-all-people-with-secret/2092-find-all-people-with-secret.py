class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            parent[find(b)] = find(a)

        meetings.sort(key=lambda x: x[2])

        union(0, firstPerson)

        i = 0
        while i < len(meetings):
            time = meetings[i][2]
            involved = []

            while i < len(meetings) and meetings[i][2] == time:
                x, y, _ = meetings[i]
                union(x, y)
                involved.append(x)
                involved.append(y)
                i += 1

            root0 = find(0)
            for p in involved:
                if find(p) != root0:
                    parent[p] = p

        return [i for i in range(n) if find(i) == find(0)]