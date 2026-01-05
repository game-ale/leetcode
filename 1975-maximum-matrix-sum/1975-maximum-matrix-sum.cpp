class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
       long long negacnt = 0,maxsum =0,zcnt=0;
        int n = matrix.size(), m= matrix[0].size(), least =100000;
        for(int i = 0;i<n;i++)
        {
            for(int j= 0;j<m;j++)
            {
                maxsum+=abs(matrix[i][j]);
                if(matrix[i][j]<0)
                {
                    negacnt++;
                }
                if(matrix[i][j]==0)
                {
                    zcnt++;
                }
                least = min(least,abs(matrix[i][j])); 
            }
        }
        if(negacnt%2==1 && zcnt ==0)
        {
            maxsum -=2*least;
        }
        return maxsum;
    }
};