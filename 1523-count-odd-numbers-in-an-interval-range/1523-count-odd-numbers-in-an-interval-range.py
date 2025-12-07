class Solution:
    def countOdds(self, low: int, high: int) -> int:
        lex = high-low
        if high%2 and low%2:
            return ((lex)//2 +1)
        elif lex%2:
            return ((lex)//2 +1)
        else:
            return ((lex)//2)
