class Solution(object):
    def countCommas(self, n):
        if n>=1000:
            return n-999
        else:
            return 0
        """
        :type n: int
        :rtype: int
        """
        