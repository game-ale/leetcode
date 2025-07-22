class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        st = set()
        ans,var  = 0,0
        left = 0
        print(Counter(nums))
        for right in range(len(nums)):
            while nums[right] in st:  
                var -= nums[left]
                st.remove(nums[left])
                left += 1
            var+=nums[right]
            st.add(nums[right])
            ans = max (ans,var)
        return ans
         
            


        