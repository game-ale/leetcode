class Solution {
public:
    bool dfs(vector<int>& arr, int i, vector<bool>& vis) {
        if (i < 0 || i >= arr.size() || vis[i]) return false;
        if (arr[i] == 0) return true;
        vis[i] = true;
        return dfs(arr, i + arr[i], vis) || dfs(arr, i - arr[i], vis);
    }

    bool canReach(vector<int>& arr, int start) {
        vector<bool> vis(arr.size(), false);
        return dfs(arr, start, vis);
    }
};