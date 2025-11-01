    public int countWays(int[][] ranges) {
        Arrays.sort(ranges, Comparator.comparingInt(r -> r[0]));
        int cnt = 1, hi = -1;
        for (int[] r : ranges) {
            if (hi < r[0]) {
                cnt <<= 1;
                cnt %= 1_000_000_007;
            }
            hi = Math.max(hi, r[1]);
        }
        return cnt;
    }