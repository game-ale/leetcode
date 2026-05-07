class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        skyline = []
        heap = []  # (height, end)
        buildings.append([inf, inf, inf])  # flusher building

        for start, end, height in buildings:
            # process buildings that have already ended
            while heap and start > heap[0][1]:
                prev_height, prev_end = heappop_max(heap)
                # discard smaller buildings that ended even earlier
                while heap and heap[0][1] <= prev_end:
                    heappop_max(heap)
                # draw right skyline point until the next tallest building or the floor
                skyline.append([prev_end, heap[0][0] if heap else 0])

            # for new buildings draw left skyline if it's above current highest
            if not heap or height > heap[0][0]:
                # same start different height case
                if skyline and skyline[-1][0] == start:
                    skyline[-1][1] = height
                else:
                    skyline.append([start, height])
            
            heappush_max(heap, (height, end))

        skyline.pop()  # pop the flusher

        return skyline

            