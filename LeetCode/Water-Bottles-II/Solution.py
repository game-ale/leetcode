class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = numBottles
        full = 0
        ans = numBottles
        
        while full + emptyBottles >= numExchange:
            if emptyBottles >= numExchange:
                emptyBottles-=numExchange
                ans +=1
                full+=1
                numExchange+=1
            else:
                emptyBottles+=full
                full = 0
        return ans
        