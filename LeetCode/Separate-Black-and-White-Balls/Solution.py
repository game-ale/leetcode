class Solution:
    def minimumSteps(self, s: str) -> int:
        t ,n= s.count('1'),len(s)
        ans = 0
        left,right = 0, n-t
        print(right)
        while left <n-t and right<n:
            while right<n and s[right]!="0":
                right+=1
            while left <n-t and s[left]!="1":
                left+=1
            if left <n-t and right<n:
                ans +=right-left
                right+=1
                left+=1
            
        
        return ans

        