class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        def find (x):
            if x%2==0:
                return -1
            i = 0
            cx = x
            while x:
                if x&1==0:
                    break
                i+=1
                x>>=1
            cx = cx & ~(1<<i-1)
            return cx
        for x in nums:
            ans.append(find(x))
        return ans
            
            

                 