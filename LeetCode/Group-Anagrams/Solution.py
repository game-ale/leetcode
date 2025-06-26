class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for word in strs:
            temp = "".join(sorted(list(word)))
            anagram[temp].append(word)
        return list(anagram.values())


        
        
        