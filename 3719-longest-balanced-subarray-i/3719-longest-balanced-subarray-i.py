class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            st = set()
            odd , even = 0, 0
            for j in range(i,n):
                if nums[j] not in st:
                    st.add(nums[j])
                    x = nums[j]%2
                    if x:
                        odd+=1
                    else:
                        even+=1
                if even==odd:
                    ans =max(ans , j-i+1)
        
        return ans 



        