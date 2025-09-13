class Solution:
    def maxFreqSum(self, s: str) -> int:
        cnt = Counter(s)
        vowel = max((cnt[c] for c in "aeiou" if c in cnt), default=0)
        cons = max((val for key, val in cnt.items() if key not in "aeiou"), default=0)
        return cons + vowel