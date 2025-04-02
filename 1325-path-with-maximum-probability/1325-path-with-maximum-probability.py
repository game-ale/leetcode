class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = {i: [] for i in range(n)}
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))

        prob_to = [0.0] * n
        prob_to[start_node] = 1.0
        heap = [(-1.0, start_node)]

        while heap:
            curr_prob, node = heapq.heappop(heap)
            curr_prob *= -1
            if node == end_node:
                return curr_prob
            if curr_prob < prob_to[node]:
                continue
            for neighbor, edge_prob in graph[node]:
                new_prob = curr_prob * edge_prob
                if new_prob > prob_to[neighbor]:
                    prob_to[neighbor] = new_prob
                    heapq.heappush(heap, (-new_prob, neighbor))

        return 0.0
