class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        val = nums[0]
        ans = []
        if val%5:
            ans.append(False)
        else:
            ans.append(True)

        for i in range(1,len(nums)):
            if nums[i]:
                val = val*2 + 1
            else:
                val = val*2
            if val%5:
                ans.append(False)
            else:
                ans.append(True)
        return ans
        

      