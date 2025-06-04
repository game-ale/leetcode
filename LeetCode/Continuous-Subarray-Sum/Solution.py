public boolean checkSubarraySum(final int[] nums, final int k) {
    var sumsSet = new HashSet<Integer>(nums.length);
    int sum = 0, prevSum;

    for (int i = 0; i < nums.length; i++) {
        prevSum = sum;
        sum = (sum + nums[i]) % k;
        if (sumsSet.contains(sum)) {
            return true;
        }
        sumsSet.add(prevSum);
    }

    return false;
}