class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def help(word):
            bit = 0
            for char in word:
                bit |= 1<<(ord(char)-ord("a"))
            return bit
        take_bit = [help(word) for word in words]
        word_len = [len(word) for word in words]
        ans = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if take_bit[i] & take_bit[j] == 0:
                    ans = max(ans , word_len[i]*word_len[j])

        return ans
                    
