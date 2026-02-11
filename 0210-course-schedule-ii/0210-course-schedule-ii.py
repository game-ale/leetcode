class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        ans = []
        for a, b in prerequisites:
            graph[b].append(a)
        indegre = [0]*numCourses
        for i in range(numCourses):
            for j in graph[i]:
                indegre[j]+=1
        q = deque()
        for i in range(numCourses):
            if indegre[i] ==0:
                q.append(i)
        while q:
            u = q.popleft()
            ans.append(u)
            for v in graph[u]:
                indegre[v]-=1
                if indegre[v]==0:
                    q.append(v)
        if len(ans)!=numCourses:
            return []
        return ans

