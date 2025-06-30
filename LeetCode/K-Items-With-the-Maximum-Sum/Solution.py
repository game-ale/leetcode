class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes >=k: 
            return k
        elif numOnes + numZeros>=k:
            return numOnes
        else:
            return (numOnes - (k - numOnes -numZeros))
        