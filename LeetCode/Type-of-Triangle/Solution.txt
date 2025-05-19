class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0]+nums[1]<=nums[2]:
            return "none"

        for i in range(len(nums)):
            if nums[0]==nums[1]== nums[2]:
                return "equilateral"

            elif nums[0]!=nums[1] and nums[1]!=nums[2] and nums[0]!=nums[2]:
                return "scalene"

            else:
                return "isosceles"
        