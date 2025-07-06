class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort()
        for st , end in intervals:
            if heap and heap[0]<st:
                heappop(heap)
            heappush(heap,end)
        return len(heap)