class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk = []
        st = set()
        cnt = defaultdict(int)
        for char in s:
            cnt[char] += 1
        for c in s:
            cnt[c]-=1
            if c in st:
                continue
            while stk and c<stk[-1] and cnt[stk[-1]]>0:
                rem_char = stk.pop()
                st.remove(rem_char)
            stk.append(c)
            st.add(c)
        return ("".join(stk))
        