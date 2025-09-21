class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.ctr = defaultdict(Counter)
        self.price = defaultdict(Counter)
        self.shops = defaultdict(SortedList)
        self.cheapest = SortedList()
        for shop, movie, price in entries:
            self.price[shop][movie] = price
            self.drop(shop, movie, True)

    def search(self, movie: int) -> List[int]:
        return [shop for price, shop in self.shops[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        self.ctr[shop][movie] -= 1
        self.cheapest.add((self.price[shop][movie], shop, movie))
        if self.ctr[shop][movie] == 0:
            self.shops[movie].remove((self.price[shop][movie], shop))

    def drop(self, shop: int, movie: int, f = False) -> None:
        self.ctr[shop][movie] += 1
        if not f:
            self.cheapest.remove((self.price[shop][movie], shop, movie))
        if self.ctr[shop][movie] == 1:
            self.shops[movie].add((self.price[shop][movie], shop))

    def report(self) -> List[List[int]]:
        return [[shop, movie] for price, shop, movie in self.cheapest[:5]]