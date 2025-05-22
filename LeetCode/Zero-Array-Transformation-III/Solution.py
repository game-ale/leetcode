public int maxRemoval(int[] nums, int[][] queries) {
    // Sort queries by their start index ascending.
    // This allows processing queries in order as we iterate through nums.
    Arrays.sort(queries, (a, b) -> a[0] - b[0]);

    // A max heap to store the right endpoints of queries that are
    // currently "active" or available. We prioritize queries that extend furthest
    // to the right, as they can potentially cover more elements.
    PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());

    // deltaArray[k] will store the net change in the number of active operations
    // at index k. It's used in a sweep-line fashion.
    // If a query [l, r] is used, it effectively adds 1 to operations from l to r.
    // This is modeled by an implicit +1 at l (when the query is chosen)
    // and an explicit -1 at r+1 (when the query's effect ends).
    int[] deltaArray = new int[nums.length + 1];

    // tracks the cumulative number of decrement operations
    // available at the current index i from the queries chosen so far.
    int operations = 0;

    // Iterate through the 'nums' array (sweep line).
    // j is an index for the sorted 'queries' array.
    for (int i = 0, j = 0; i < nums.length; i++) {
        // Update 'operations' based on deltaArray.
        // This incorporates the effect of queries starting or ending at index i.
        // For example, if a chosen query ended at i-1, deltaArray[i] would
        // contain a -1 to decrease the active operations count.
        operations += deltaArray[i];

        // Add newly available queries to the heap.
        // These are queries whose start index is equal to the current index i.
        // We add their right endpoints to the max-heap.
        while (j < queries.length && queries[j][0] == i) {
            heap.offer(queries[j][1]);
            j++;
        }

        // Satisfy nums[i] using available queries.
        // If the current number of 'operations' is less than nums[i],
        // we need to "activate" more queries to decrement nums[i].
        while (
                operations < nums[i] && // Still need more decrements for nums[i]
                !heap.isEmpty() &&      // There are available queries
                heap.peek() >= i        // The best available query covers index i
        ) {
            // "Use" the query that extends furthest to the right.
            // This is a greedy choice: pick the query that can cover the current
            // element and potentially many subsequent elements.
            operations += 1;

            // Schedule the end of this query's effect.
            // The query whose right endpoint is heap.poll() is now "chosen".
            // Its effect of +1 operation will end after its right endpoint.
            // So, we subtract 1 from deltaArray at (endpoint + 1).
            deltaArray[heap.poll() + 1] -= 1;
        }

        // If, after trying to use available queries, we still can't satisfy nums[i],
        // then it's impossible to make nums[i] zero.
        if (operations < nums[i]) {
            return -1;
        }
    }

    // At this point, if a solution was found, the 'heap' contains the right
    // endpoints of queries that were offered (their start index was encountered)
    // but were never "chosen" or "used" (polled from the heap).
    // These are the queries that were not needed by the greedy strategy
    // to make 'nums' a zero array. Thus, they can be removed.
    // The size of the heap represents the maximum number of queries
    // that can be removed.
    return heap.size();
}