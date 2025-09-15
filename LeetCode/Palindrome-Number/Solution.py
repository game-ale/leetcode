class Solution:
    def isPalindrome(self, num: int) -> bool:
        if num<0:
            return False
        else:
            t = str(num)
            if int(t[::-1])==num:
                return True
        return False