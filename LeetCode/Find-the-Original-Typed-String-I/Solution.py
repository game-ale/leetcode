class Solution:
    def possibleStringCount(self, word: str) -> int:
        stk = []
        for c in word:
            if stk and c==stk[-1]:
                continue
            stk.append(c)
        return (len(word) - len(stk) +1)
        