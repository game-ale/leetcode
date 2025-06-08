class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        for start in range(1, 10):
            self.generate(start, n, ans)
        return ans

    def generate(self, cur, limit, result):
        if cur > limit:
            return
        result.append(cur)
        for num in range(10):
            num = cur * 10 + num
            if num <= limit:
                self.generate(num, limit, result)
            else:
                break  