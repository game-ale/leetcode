        while(i<n) {
            mpp[nums[i]]++;
            while(mpp.size() > k) {
                mpp[nums[j]]--;
                if(mpp[nums[j]] == 0) {
                    mpp.erase(nums[j]);
                }
                j++;
            }
            noOfSubarrays += i-j+1;
            i++;
        }
    return noOfSubarrays;
}
int subarraysWithKDistinct(vector<int>& nums, int k) {
    return atMost(nums, k) - atMost(nums, k-1);
}