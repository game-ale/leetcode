class Solution(object):
    def totalNumbers(self, digits):
        st = set()
        n = len(digits)
        for k in range(n):
            if digits[k]%2==0:
                for i in range(n):
                    if digits[i]!=0 and i!=k:
                        for j in range(n):
                            if j!=i and j!=k:
                                st.add(digits[i]*100 + digits[j]*10 + digits[k] )
        return len(st)

        """
        :type digits: List[int]
        :rtype: int
        """
        