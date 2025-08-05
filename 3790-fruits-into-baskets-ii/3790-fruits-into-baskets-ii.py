class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n, m = len(fruits), len(baskets)
        cnt = 0
        
        for i in range(n):
            x = fruits[i]
            flag = False
            for j in range(m):  
                if baskets[j] >= x:
                    baskets[j] = -1 
                    flag = True
                    break 
            if not flag:
                cnt += 1  
        
        return cnt
