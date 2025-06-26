class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])
        ans = []  
        for j in range(1,len(words)):
            cnt1 = Counter(words[j])
            for char in list(cnt.keys()):  
                if char in cnt1:
                    cnt[char] = min(cnt[char], cnt1[char])
                else:
                    del cnt[char] 
        for key, val in cnt.items():
            for i in range(val):
                ans.append(key)
        return ans


            

        