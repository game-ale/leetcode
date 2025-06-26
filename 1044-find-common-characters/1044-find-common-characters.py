class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])
        ans = []
        for word in words[1:]:
            cnt1 = Counter(word)
            cnt &= cnt1
        for key, val in cnt.items():
            ans.extend([key]*val)
        return ans

        