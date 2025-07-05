class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        cnt =  Counter(arr)
        for key, val in cnt.items():
            if key == val:
                ans  = max(ans, val)
        return ans