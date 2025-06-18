class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        if n<3:
            return []
        i = 0
        while i < n:
            temp = nums[i:i+3]
            if temp[-1] - temp[0] <=k:
                ans.append(temp)
                i+=3
            else:
                return []
        return ans
        

        