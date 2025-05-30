class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        while edges[node1] >= 0 or edges[node2] >= 0:
            if edges[node1] >= 0:
                temp = node1
                node1 = edges[node1]
                edges[temp] = -3
            if edges[node2] >= 0:
                temp = node2
                node2 = edges[node2]
                edges[temp] = -2
            if edges[node1] == -2 and edges[node2] == -3:
                return min(node1, node2)
            if edges[node1] == -2:
                return node1
            if edges[node2] == -3:
                return node2

        return node1 if node1 == node2 else -1
