class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = 0
        diagonal = 0.0
        for a , b in dimensions:
            temp = (a**2 + b**2)**0.5
            if temp > diagonal:
                ans = a*b
                diagonal = temp
            elif temp == diagonal:
                ans = max(ans,a*b)
        return ans



        