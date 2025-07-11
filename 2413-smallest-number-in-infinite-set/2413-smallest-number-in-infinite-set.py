class SmallestInfiniteSet:
    def __init__(self):
        self.added_back = []
        self.added_set = set()
        self.current = 1

    def popSmallest(self) -> int:
        if self.added_back:
            smallest = heapq.heappop(self.added_back)
            self.added_set.remove(smallest)
            return smallest
        else:
            smallest = self.current
            self.current += 1
            return smallest

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.added_set:
            heapq.heappush(self.added_back, num)
            self.added_set.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)