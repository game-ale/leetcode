class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row, col = len(mat),len(mat[0])
        ans = []
        for k in range (row+col-1):
            temp = []
            i = 0 if k<col else k - col +1
            j = k if k<col else col - 1
            while i<row and j>=0:
                temp.append(mat[i][j])
                i+=1
                j-=1
            if k%2==0:
                temp = temp[::-1]
            ans.extend(temp)
        return ans

        
            


    
            
        
        