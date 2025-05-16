class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1] * n
        mask = [(1 << i) for i in range(n)]

        def ham_distance(wrd1, wrd2):
            dis = 0
            for a, b in zip(wrd1, wrd2):
                if a != b:
                    dis +=1

            return dis


        best_mask = 1
        best_seq = 1

        for i in range(n):
            for j in range(i):
                if len(words[j]) == len(words[i]) \
                 and groups[j] != groups[i] \
                 and ham_distance(words[i], words[j]) == 1:
                    
                    if dp[j] + 1 > dp[i]:

                        dp[i] =  dp[j] + 1
                        mask[i] = mask[j] | (1 << i)
                        if dp[i] > best_seq:
                            best_seq = dp[i]
                            best_mask = mask[i]

        ans = []
        i = 0
        while best_mask:
            if best_mask & 1:
                ans.append(words[i])
            
            i +=1
            best_mask >>= 1


        return ans