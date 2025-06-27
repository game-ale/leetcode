class Solution(object):
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        
        flat = [num for row in mat for num in row]
        return [flat[i * c:(i + 1) * c] for i in range(r)]