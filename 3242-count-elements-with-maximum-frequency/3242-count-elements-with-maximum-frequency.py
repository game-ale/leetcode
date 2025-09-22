class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num = Counter(nums)
        cnt = [val for key, val in num.items()]
        high = max(cnt)
        temp = cnt.count(high)
        return temp*high
        