class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = defaultdict(list)
        for word in strs:
            temp = "".join(sorted(list(word)))
            anag[temp].append(word)
        return list(anag.values())


        
        
        