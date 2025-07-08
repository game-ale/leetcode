class Solution {
public:
    int maxValue(vector<vector<int>>& events, int k) {
        sort(events.begin(), events.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        int n = events.size();
        vector<vector<int>> dp(k + 1, vector<int>(n, -1));
        return dfs(0, 0, -1, events, k, dp);
    }
    
    int dfs(int curIndex, int count, int prevEndingTime, vector<vector<int>>& events, int k, vector<vector<int>>& dp) {
        if (curIndex == events.size() || count == k) {
            return 0;
        }
        
        if (prevEndingTime >= events[curIndex][0]) {
            return dfs(curIndex + 1, count, prevEndingTime, events, k, dp);
        }
        
        if (dp[count][curIndex] != -1) {
            return dp[count][curIndex];
        }
        
        int ans = max(dfs(curIndex + 1, count, prevEndingTime, events, k, dp),
                      dfs(curIndex + 1, count + 1, events[curIndex][1], events, k, dp) + events[curIndex][2]);
        dp[count][curIndex] = ans;
        return ans;
    }
};
 