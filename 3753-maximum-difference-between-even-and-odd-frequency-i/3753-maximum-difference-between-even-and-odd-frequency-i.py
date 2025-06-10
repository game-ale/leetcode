class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        even,odd = len(s),0
        for _ ,val in cnt.items():
            if val%2==0:
                even = min(even,val)
            else:
                odd = max(odd,val)
        return(odd-even)