class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        # Create a graph representation of character conversions
        adjacency_list = [[] for _ in range(26)]

        # Populate the adjacency list with character conversions
        conversion_count = len(original)
        for i in range(conversion_count):
            adjacency_list[ord(original[i]) - ord("a")].append(
                (ord(changed[i]) - ord("a"), cost[i])
            )

        # Calculate shortest paths for all possible character conversions
        min_conversion_costs = [
            self._dijkstra(i, adjacency_list) for i in range(26)
        ]

        # Calculate the total cost of converting source to target
        total_cost = 0
        for s, t in zip(source, target):
            if s != t:
                char_conversion_cost = min_conversion_costs[ord(s) - ord("a")][
                    ord(t) - ord("a")
                ]
                if char_conversion_cost == float("inf"):
                    return -1  # Conversion not possible
                total_cost += char_conversion_cost

        return total_cost

    def _dijkstra(
        self, start_char: int, adjacency_list: List[List[tuple]]
    ) -> List[int]:
        # Priority queue to store characters with their conversion cost, sorted by cost
        priority_queue = [(0, start_char)]

        # List to store the minimum conversion cost to each character
        min_costs = [float("inf")] * 26

        while priority_queue:
            current_cost, current_char = heapq.heappop(priority_queue)

            if min_costs[current_char] != float("inf"):
                continue

            min_costs[current_char] = current_cost

            # Explore all possible conversions from the current character
            for target_char, conversion_cost in adjacency_list[current_char]:
                new_total_cost = current_cost + conversion_cost

                # If we found a cheaper conversion, update its cost
                if min_costs[target_char] == float("inf"):
                    heapq.heappush(
                        priority_queue, (new_total_cost, target_char)
                    )

        # Return the list of minimum conversion costs from the starting character to all others
        return min_costs