class Solution:
    def isPrerequisite(
        self, adjList: dict, visited: List[bool], src: int, target: int
    ) -> bool:
        visited[src] = True
        if src == target:
            return True
        for adj in adjList.get(src, []):
            if not visited[adj]:
                if self.isPrerequisite(adjList, visited, adj, target):
                    return True
        return False

    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        adjList = {i: [] for i in range(numCourses)}
        for edge in prerequisites:
            adjList[edge[0]].append(edge[1])

        result = []
        for query in queries:
            visited = [False] * numCourses
            result.append(
                self.isPrerequisite(adjList, visited, query[0], query[1])
            )
        return result
