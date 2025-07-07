class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        top_two = sorted(freq.items(), key=lambda item: item[1], reverse=True)[:2]
        return [num for num, _ in top_two]
