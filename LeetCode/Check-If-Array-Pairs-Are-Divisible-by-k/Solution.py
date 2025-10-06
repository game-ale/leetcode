class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainderCount = [0] * k
        for num in arr:
            remainderCount[num % k] += 1
        if remainderCount[0] % 2:
            return False
        for i in range(1, k // 2 + 1):
            if remainderCount[i] != remainderCount[k - i]:
                return False
        return True