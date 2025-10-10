class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        num = heights.copy()
        num.sort()
        ans = 0
        for i in range(len(num)):
            if num[i]!= heights[i]:
                ans+=1
        return ans

        