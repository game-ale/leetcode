class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        transpose = [[0]*rows for _ in range(cols)]
        print(transpose)
        for i in range(cols):
            for j in range(rows):
                transpose[i][j] = matrix[j][i]
        return transpose
                
            

            
               
        