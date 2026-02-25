class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        cnt = defaultdict(list)
        st = set()
        for num in arr:
            x = bin(num).count("1")
            cnt[x].append(num)
            st.add(x)
    
        st = list(st)
        st.sort()
        ans = []
        for s  in st:
            cnt[s].sort()
            ans.extend(cnt[s])
        return ans
