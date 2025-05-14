class Solution(object):
    def lengthAfterTransformations(self, s, t, nums):
        mod = 10**9+7
        A = [[0]*26 for _ in range(26)]
        for j in range(26):
            for k in range(1, nums[j]+1):
                A[(j+k)%26][j] = 1

        def matmul(X, Y):
            Z = [[0]*26 for _ in range(26)]
            for i in range(26):
                for k in range(26):
                    if X[i][k]:
                        for j in range(26):
                            Z[i][j] = (Z[i][j] + X[i][k]*Y[k][j]) % mod
            return Z

        def matpow(Mn, e):
            R = [[1 if i==j else 0 for j in range(26)] for i in range(26)]
            while e:
                if e & 1:
                    R = matmul(R, Mn)
                Mn = matmul(Mn, Mn)
                e >>= 1
            return R

        M = matpow(A, t)
        v = [0]*26
        for c in s:
            v[ord(c)-97] += 1

        res = 0
        for i in range(26):
            for j in range(26):
                res = (res + M[i][j]*v[j]) % mod
        return res