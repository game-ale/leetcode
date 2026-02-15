class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []  

        i, j, carry = len(a) - 1, len(b) - 1, 0

        while i >= 0 or j >= 0 or carry:

            digit_a = int(a[i]) if i >= 0 else 0

            digit_b = int(b[j]) if j >= 0 else 0

            sum = digit_a + digit_b + carry

            result.append(str(sum % 2))

            carry = sum // 2

            i, j = i - 1, j - 1

        return ''.join(reversed(result))
        