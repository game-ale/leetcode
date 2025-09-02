class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cnt = Counter(s)
        st = set()
        for key, val in cnt.items():
            st.add(val)
        return len(st)==1 or len(st)==0
        
        