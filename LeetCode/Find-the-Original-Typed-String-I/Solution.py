class Solution:
    def possibleStringCount(self, word: str) -> int:
        return sum(word[i - 1] == word[i] for i in range(1, len(word))) + 1