class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 1:
            half = n // 2
            ans = [x for x in range(-half, half+1)]
        else:
            half = n // 2
            ans = [x for x in range(-half, 0)] + [y for y in range(1, half+1)]
        return ans
        