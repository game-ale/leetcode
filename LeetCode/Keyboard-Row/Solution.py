class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        start = "qwertyuiop"
        start = set(start)
        second = "asdfghjkl"
        second = set(second)
        third  = "zxcvbnm"
        third = set(third)
        for word in words:
            temp = set(word.lower())
            if temp.issubset(start) or temp.issubset(second) or temp.issubset(third):
                ans.append(word)
        return ans