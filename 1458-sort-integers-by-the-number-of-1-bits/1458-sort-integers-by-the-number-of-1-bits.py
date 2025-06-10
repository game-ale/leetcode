class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ones = 0
        ans = []
        for num in arr:
            ones = max(ones , bin(num).count("1"))
        cnt = [[] for _ in range(ones +1)]
        for num in arr:
            cnt[bin(num).count("1")].append(num)
        for i in range(ones+1):
            cnt[i].sort()
        for i in range(ones+1):
            ans.extend(cnt[i])
        
        return ans

        
        