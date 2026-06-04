class Solution:
    MAX = 100005
    dp = [0] * MAX
    pref = [0] * MAX

    for i in range(100, MAX):
        d1 = i % 10
        d2 = (i // 10) % 10
        d3 = (i // 100) % 10

        wave = int(d2 > max(d3, d1) or d2 < min(d3, d1))

        dp[i] = dp[i // 10] + wave
        pref[i] = pref[i - 1] + dp[i]

    def totalWaviness(self, A: int, B: int) -> int:
        return self.pref[B] - self.pref[A - 1]
