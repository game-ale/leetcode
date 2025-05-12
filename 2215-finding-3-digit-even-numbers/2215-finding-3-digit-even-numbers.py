class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        st = set()
        digits.sort()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if not(i == k or j== i or k==j) and digits[k] % 2 == 0 and digits[i] != 0:
                    
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                        st.add(num)
                    
        return sorted(list(st))
        