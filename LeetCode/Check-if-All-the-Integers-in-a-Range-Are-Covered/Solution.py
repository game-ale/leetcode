class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        firstset = set()
        secondset = set()
        for  rang in ranges:
            for j in range(rang[0],rang[1]+1):
                firstset.add(j)
        for i in range (left,right+1):
            secondset.add(i)
        if secondset.issubset(firstset):
            return True
        return False