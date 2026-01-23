class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left , right = 0,int(sqrt(c))
        if c<=1:
            return True
        while left < right:
            sleft = left*left
            sright = right*right
            if sleft + sright == c:
                return True
            if sleft + sright > c:
                right-=1
            else:
                left-=1
        return False
            
        