class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        temp = []
        for row in bank:
            if row.count('1'):
                temp.append(row.count("1"))
        ans = 0
        for i in range(1,len(temp)):
            ans+=(int(temp[i])* int(temp[i-1]))
        return ans


        