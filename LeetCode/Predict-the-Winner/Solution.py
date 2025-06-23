class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(left, right):
            if left == right:
                return nums[left]
            return max(
                nums[left]  - dfs(left + 1, right),
                nums[right] - dfs(left, right - 1)
            )
        return dfs(0, len(nums) - 1) >= 0