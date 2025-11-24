class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        third = len(nums)/3
        ans = []
        for key,val in cnt.items():
            if val > third:
                ans.append(key)
        return ans
        