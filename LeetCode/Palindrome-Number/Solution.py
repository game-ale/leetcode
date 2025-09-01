class Solution:
    def isPalindrome(self, val: int) -> bool:
        if val<0:
            return False
        else:
            t = str(val)
            if int(t[::-1])==val:
                return True
        return False