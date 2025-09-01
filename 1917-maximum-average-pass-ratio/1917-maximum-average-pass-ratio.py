class Solution:
    def calculateGain(self, pass_students, total_students):
        return (pass_students + 1) / (total_students + 1) - pass_students / total_students
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap = []
        total_sum = 0.0

        for passed, total in classes:
            total_sum += passed / total
            gain = self.calculateGain(passed, total)
            heapq.heappush(max_heap, (-gain, passed, total))

        for _ in range(extraStudents):
            neg_gain, passed, total = heapq.heappop(max_heap)
            total_sum -= passed / total
            passed += 1
            total += 1
            total_sum += passed / total
            new_gain = self.calculateGain(passed, total)
            heapq.heappush(max_heap, (-new_gain, passed, total))

        return total_sum / len(classes)


        