class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = []
        prev = 0
        for num in pref:
            ans.append(num^prev)
            prev = num
        return ans