class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def Divisors(num:int) -> List[int]:
            i = 1
            ans = []
            x = int(num**0.5)+1
            for i in range(1,x):
                if num%i==0:
                    ans.append(i)
                    if i*i!=num:
                        ans.append(num//i)
                if len(ans)>5:
                    return []
            return ans
        res = 0
        for num in nums:
            temp = Divisors(num)
            if len(temp)==4:
                res+=sum(temp)
        return res
                

        