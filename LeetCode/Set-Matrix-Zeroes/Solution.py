class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_dict = defaultdict(set)
        cols_dict = defaultdict(set)

        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                val = matrix[row][col]
                if val == 0:
                    rows_dict[row].add(val)
                    cols_dict[col].add(val)

        for row in range(rows):
            for col in range(cols):
                if row in rows_dict or col in cols_dict:
                    matrix[row][col] = 0

        return matrix
