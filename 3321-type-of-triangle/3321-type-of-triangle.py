class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        a, b ,c = nums
        if a == c:
            return "equilateral"
        elif c >= a+b:
            return "none"
        elif a==b or b ==c:
            return "isosceles"
        else:
            return "scalene"
        