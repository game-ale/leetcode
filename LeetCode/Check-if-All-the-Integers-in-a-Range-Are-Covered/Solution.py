class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        set1 = set()
        set2 = set()
        for  rang in ranges:
            for j in range(rang[0],rang[1]+1):
                set1.add(j)
        for i in range (left,right+1):
            set2.add(i)
        if set2.issubset(set1):
            return True
        return False
        