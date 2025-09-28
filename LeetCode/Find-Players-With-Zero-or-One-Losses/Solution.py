class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        count = Counter()
        ans = [[],[]]
        for m,n in matches:
            if m not in count:
                count[m] = 0
            count[n]+=1
        for x, y in count.items():
            if y<2:
                ans[y].append(x)
        ans[0].sort()
        ans[1].sort()
        return ans



             
        