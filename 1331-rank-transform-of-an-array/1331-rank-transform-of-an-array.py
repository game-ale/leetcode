class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        st = list(set(arr))

        st.sort()
        dic = {}
        ans =  []
        for i in range(len(st)):
            dic[st[i]] = i+1
        for i in range (len(arr)):
            ans.append(dic[arr[i]])
        return ans

        return []
        