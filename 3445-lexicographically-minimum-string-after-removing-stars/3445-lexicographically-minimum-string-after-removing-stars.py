class Solution:
    def clearStars(self, s: str) -> str:
        cnt = [[] for i in range (26)]
        ans  = list(s)
        for  i  in range (len(s)):
            if ans[i]!="*":
                cnt[ord(ans[i])-ord("a")].append(i)
            else:
                for j in range (26):
                    if cnt[j]:
                        ans[cnt[j].pop()] = "*"
                        break
        return "".join(c for c in ans if c!="*")





        