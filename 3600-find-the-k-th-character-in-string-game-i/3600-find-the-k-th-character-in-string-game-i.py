class Solution:
    def kthCharacter(self, k: int) -> str:
        n = ceil(math.log2(k))
        ans = [0]
        for i in range(n):
            temp = []
            for j in range(len(ans)):
                l = (ans[j]+1)%26
                temp.append(l)
            ans = ans + temp
        
        return chr(ans[k-1] +97)




        