class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vol = {'a','e','o','i','u'}
        n = len(words)
        pre = [0]*(n+1)
        ans = []
        for i in range(1,n+1):
            if words[i-1][0] in vol and words[i-1][-1] in vol:
                pre[i] =  pre[i-1]+1
            else:
                pre[i]= pre[i-1]

        for a, b in queries:
            ans.append(pre[b+1]-pre[a])

   

        return ans
        