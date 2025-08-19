class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans , temp = 0,0
        for num in nums:
            if num == 0:
                temp+=1
                ans+=temp
            else:
                temp = 0
        return ans

            
                
        