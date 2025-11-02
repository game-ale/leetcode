class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        color = [0] * (n + 1)  
        
        for i in range(1, n + 1):
            if color[i] == 0:
                queue = deque([i])
                color[i] = 1
                while queue:
                    cur = queue.popleft()
                    for neighbor in graph[cur]:
                        if color[neighbor] == 0:
                            color[neighbor] = -color[cur]
                            queue.append(neighbor)
                        elif color[neighbor] == color[cur]:
                            return False
        return True