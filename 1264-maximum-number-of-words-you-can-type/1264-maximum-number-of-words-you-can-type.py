class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0
        words  = text.split()
        for word in words:
            if Counter(word)-Counter(brokenLetters) == Counter(word):
                res +=1
        return res
        