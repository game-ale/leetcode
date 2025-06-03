class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        res = 0
        q = deque(initialBoxes)
        visit = set()
        while q:
            for i in range(len(q)):
                curBox = q.popleft()
                if curBox in visit:
                    continue
                visit.add(curBox)
                
                if status[curBox]:
                    res += candies[curBox]
                    for k in keys[curBox]:
                        if k in visit and status[k] == 0:
                            status[k] = 1
                            q.append(k)
                            visit.remove(k)
                        else:
                            status[k] = 1
                    for box in containedBoxes[curBox]:
                        q.append(box)
        return res