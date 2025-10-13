class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stk = [words[0]]
        for word in words[1:]:
            if Counter(word)== Counter(stk[-1]):
                continue
            else:
                stk.append(word)
        return stk
        