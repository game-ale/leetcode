class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        ans = [float(num) for num in cards]
        return self.backtrack(ans)
    def backtrack(self, ans: List[float]) -> bool:
        if len(ans)==1:
            return abs(ans[0]-24.0)<1e-6
        n = len(ans)
        for i in range(n):
            for j in range(n):
                if i!=j:
                    nextans = [ans[k] for k in range(n)if k!=i and k!=j]
                    a,b = ans[i],ans[j]
                    res = [a+b,a-b,b-a,a*b]
                    if abs(a)>1e-6:
                        res.append(b/a)
                    if abs(b)>1e-6:
                        res.append(a/b)
                    for val in res:
                        if self.backtrack(nextans + [val]):
                            return True
        return False


        