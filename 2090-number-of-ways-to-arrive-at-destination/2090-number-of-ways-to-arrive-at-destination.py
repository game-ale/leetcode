
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        INF = inf
        MODULO = 10**9 + 7
        graph = [[INF] * n for _ in range(n)]
        
        for start, end, time in roads:
            graph[start][end] = time
            graph[end][start] = time
        
        graph[0][0] = 0
        min_distance = [INF] * n
        path_count = [0] * n
        min_distance[0] = 0
        path_count[0] = 1
        visited = [False] * n
        
        for _ in range(n):
            current = -1
            for i in range(n):
                if not visited[i] and (current == -1 or min_distance[i] < min_distance[current]):
                    current = i
            
            visited[current] = True
            
            for neighbor in range(n):
                if neighbor == current:
                    continue
                
                new_distance = min_distance[current] + graph[current][neighbor]
                
                if min_distance[neighbor] > new_distance:
                    min_distance[neighbor] = new_distance
                    path_count[neighbor] = path_count[current]
                elif min_distance[neighbor] == new_distance:
                    path_count[neighbor] += path_count[current]
        
        return path_count[-1] % MODULO