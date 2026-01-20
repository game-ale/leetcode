class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        x = n
        while True:
            ans = 0
            while x:
                ans +=((x%10)**2)
                x//=10
            x = ans
            print(ans)

            if ans == 1:
                return True 
            if ans in seen:
                return False
            seen.add(ans)




        