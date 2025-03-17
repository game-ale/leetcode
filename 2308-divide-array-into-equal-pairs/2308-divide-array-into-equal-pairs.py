class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        if any(cnt[key]%2==1 for key in cnt):
            return False
        return True
        