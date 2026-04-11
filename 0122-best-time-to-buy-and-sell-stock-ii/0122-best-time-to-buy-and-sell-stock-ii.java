class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int min = Integer.MAX_VALUE;
        for(int i = 0; i < prices.length; i++)
        {
            if(min > prices[i])
            {
                min = prices[i];
            }
            else
            {
                profit += prices[i] - min;
                min = prices[i];           
            }
        }        
        return profit;
    }
}