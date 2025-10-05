class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        first = "qwertyuiop"
        first = set(first)
        second = "asdfghjkl"
        second = set(second)
        third  = "zxcvbnm"
        third = set(third)
        for word in words:
            temp = set(word.lower())
            if temp.issubset(first) or temp.issubset(second) or temp.issubset(third):
                ans.append(word)
        return ans
        