class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def can_split(intervals: List[List[int]]) -> bool:
            intervals.sort()
            cuts = 0
            current_end = intervals[0][1]
            for start, end in intervals[1:]:
                if start >= current_end:
                    cuts += 1
                    if cuts >= 2:
                        return True
                current_end = max(current_end, end)
            return False

        x_intervals = [[rect[0], rect[2]] for rect in rectangles]
        y_intervals = [[rect[1], rect[3]] for rect in rectangles]

        return can_split(x_intervals) or can_split(y_intervals)
