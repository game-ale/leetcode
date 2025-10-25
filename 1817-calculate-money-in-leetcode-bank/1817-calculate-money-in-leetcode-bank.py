class Solution:
    def totalMoney(self, n: int) -> int:
        div , rem, cnt = n//7, n%7,n//7-1
        ans = 28*div + (cnt*div*7/2 if cnt>0 else 0)
        temp = (div*rem) + rem*(rem + 1)//2
        return int(ans + temp)



        