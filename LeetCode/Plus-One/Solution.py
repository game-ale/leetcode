class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]<=8:
            digits[-1]+=1
            return digits
        ans = str(int("".join(map(str,digits)))+1)
        res = []
        for char in ans:
            res.append(int(char))
        return res
        

        