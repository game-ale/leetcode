class SmallestInfiniteSet:
    def __init__(self):
        self.arr = []
        heapify(self.arr)
        self.ceiling = 1

    def popSmallest(self) -> int:
        if len(self.arr) == 0:
            self.ceiling += 1
            return self.ceiling - 1
        else:
            return heappop(self.arr)

    def addBack(self, num: int) -> None:
        if num < self.ceiling:
            heappush(self.arr, num)