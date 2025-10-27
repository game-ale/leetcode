class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        temp1 , temp2 = 0,0 
        for row in bank:
            if row.count('1'):
                temp1 = temp2
                temp2 = row.count('1')
                ans+=(temp1*temp2)
        return ans


        