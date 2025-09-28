class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        cnt = Counter()
        ans = [[],[]]
        for m,n in matches:
            if m not in cnt:
                cnt[m] = 0
            cnt[n]+=1
        for x, y in cnt.items():
            if y<2:
                ans[y].append(x)
        ans[0].sort()
        ans[1].sort()
        return ans