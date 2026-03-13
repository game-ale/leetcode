class Solution:
    def minNumberOfSeconds(
        self, mountainHeight: int, workerTimes: List[int]
    ) -> int:
        maxWorkerTimes = max(workerTimes)
        l, r, ans = (
            1,
            maxWorkerTimes * mountainHeight * (mountainHeight + 1) // 2,
            0,
        )
        eps = 1e-7

        while l <= r:
            mid = (l + r) // 2
            cnt = 0
            for t in workerTimes:
                work = mid // t
                # find the largest k such that 1+2+...+k <= work
                k = int((-1 + ((1 + work * 8) ** 0.5)) / 2 + eps)
                cnt += k
            if cnt >= mountainHeight:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans