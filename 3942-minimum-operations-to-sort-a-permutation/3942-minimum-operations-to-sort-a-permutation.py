class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        start = nums.index(0)

        asc = True
        desc = True

        for i in range(1, n):
            value = nums[(start + i) % n]

            if value != i:
                asc = False
            if value != n - i:
                desc = False

            if not asc and not desc:
                return -1

        if asc:
            return min(start, n - start + 2)

        return min(n - start, start + 2)