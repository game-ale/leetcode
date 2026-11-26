class Solution:
    def canAliceWin(self, n: int) -> bool:
        x = 9
        if n<10:
            return False
        n-=10
        while n and n>=x:
            
            n-=x
            x-=1
        if x%2:
            return True
        else:
            return False
        

        