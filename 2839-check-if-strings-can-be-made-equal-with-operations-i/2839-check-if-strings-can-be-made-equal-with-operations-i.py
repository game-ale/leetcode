class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        ls, ls1 = list(s1) , list(s2)
        for i in range(4):
            if ls[i]!=ls1[i] and ls[i]!=ls1[(i+2)%4]:
                return False
        return True

        