class Solution {
   public String getHappyString(int n, int k) {
       k--;
       int num1 = k >> (n - 1);
       if (num1 > 2) {
           return "";
       }

       String s = "" + ((char) ('a' + num1));
       for (int pos = n - 2; pos >= 0; pos--) {
           int bit = (k >> pos) & 1;
           char prev = s.charAt(s.length() - 1);
           char next = bit == 0 ? prev == 'a' ? 'b' : 'a'
                                : prev == 'c' ? 'b' : 'c';
           s += next;
       }
       return s;
   }
}