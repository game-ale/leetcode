class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        first = set()
        second = set()
        for  rang in ranges:
            for j in range(rang[0],rang[1]+1):
                first.add(j)
        for i in range (left,right+1):
            second.add(i)
        if second.issubset(first):
            return True
        return False