class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        ans = len(word)
        cnt1 = Counter(word)
        arr = [v for v in cnt1.values()]
        for i in range(len(arr)):
            delete  = 0
            for j in range(len(arr)):
                if arr[i]>arr[j]:
                    delete+=(arr[j])
                elif arr[j]>arr[i] + k:
                    delete+=(arr[j]-(arr[i]+k))
            ans= min(ans,delete)
        return ans

        