class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int n=nums.size();
        int subset=pow(2,n);
        vector<vector<int>>ans;
        for(int i=0;i<=subset-1;i++)
        {
            vector<int>ds;
            for(int j=0;j<=n-1;j++)
            {
                if(i&(1<<j))
                {
                  ds.push_back(nums[j]);  
                }
            }
        ans.push_back(ds);
        }
        return ans;
    }
};