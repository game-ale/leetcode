
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        last_bit = -1
        ans = []
        for i in range(len(groups)):
            if groups[i] != last_bit:
                ans.append(words[i])
            last_bit = groups[i]

        return ans