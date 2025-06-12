class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = defaultdict(int)
        for i in range(len(nums)):
            if target-nums[i] in check:
                return [check[target-nums[i]],i] 
            check[nums[i]] = i
        return []
        