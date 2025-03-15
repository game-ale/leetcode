class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            t = str(x)
            if int(t[::-1])==x:
                return True
        return False
        