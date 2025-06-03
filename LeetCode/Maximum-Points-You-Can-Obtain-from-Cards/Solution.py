class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = 0
        pre = [total := total+num for num in cardPoints]
        ans = 0
        n = len(cardPoints)
        for i in range(k+1):
            front = pre[i-1] if i>0 else 0
            back = pre[-1] - pre[n-(k-i)-1] if k-i>0 else 0
            ans = max ( ans, back + front)
        print(ans)
        return ans


    