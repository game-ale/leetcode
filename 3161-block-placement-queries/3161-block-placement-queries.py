class Solution:
    def __init__(self):
        self.seg = []
        self.st = SortedList()
        self.mx = 50000

    def update(self, idx: int, val: int, p: int, l: int, r: int) -> None:
        if l == r:
            self.seg[p] = val
            return

        mid = (l + r) >> 1
        if idx <= mid:
            self.update(idx, val, p << 1, l, mid)
        else:
            self.update(idx, val, p << 1 | 1, mid + 1, r)

        self.seg[p] = max(self.seg[p << 1], self.seg[p << 1 | 1])

    def query(self, L: int, R: int, p: int, l: int, r: int) -> int:
        if L <= l and r <= R:
            return self.seg[p]

        mid = (l + r) >> 1
        res = 0
        if L <= mid:
            res = max(res, self.query(L, R, p << 1, l, mid))
        if R > mid:
            res = max(res, self.query(L, R, p << 1 | 1, mid + 1, r))

        return res

    def getResults(self, queries: List[List[int]]) -> List[bool]:
        self.mx = 50000
        self.seg = [0] * (self.mx << 2)
        self.st = SortedList([0, self.mx])
        self.update(self.mx, self.mx, 1, 0, self.mx)
        ans = []

        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = min(len(self.st) - 1, self.st.bisect_right(x))

                r = self.st[idx]
                l = self.st[idx - 1] if idx > 0 else self.st[0]
                self.update(x, x - l, 1, 0, self.mx)
                self.update(r, r - x, 1, 0, self.mx)
                self.st.add(x)
            else:
                x, sz = q[1], q[2]
                idx = min(len(self.st) - 1, self.st.bisect_right(x))
                pre = self.st[0] if idx == 0 else self.st[idx - 1]

                max_space = max(x - pre, self.query(0, pre, 1, 0, self.mx))
                ans.append(max_space >= sz)

        return ans