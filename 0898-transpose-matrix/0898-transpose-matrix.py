class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        answer = [[0]*rows for _ in range(cols)]
        print(answer)
        for i in range(cols):
            for j in range(rows):
                answer[i][j] = matrix[j][i]
        return answer
                
            

            
               
        