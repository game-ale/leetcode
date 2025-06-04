class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rem = [num%k for num in arr]
        rem.sort()
      
        zero = rem.count(0)
        if zero%2!=0:
            return False
        left = zero
        right = len(arr)-1
        while left<right:
            if (rem[left] + rem[right])%k!=0:
                return False
            left+=1
            right-=1
        return True

        