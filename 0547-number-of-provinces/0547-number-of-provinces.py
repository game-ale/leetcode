class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for neighbor in range(len(isConnected)):
                if isConnected[node][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        visited = set()
        provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                visited.add(i)
                dfs(i)
                provinces += 1

        return provinces

        