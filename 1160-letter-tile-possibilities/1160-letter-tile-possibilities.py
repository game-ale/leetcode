class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        def dfs (cnt : Counter):
            ans = 0
            for key, val in cnt.items():
                if val > 0:
                    ans+=1
                    cnt[key]-=1
                    ans+=dfs(cnt)
                    cnt[key]+=1
            return ans
        cnt = Counter(tiles)
        return (dfs(cnt))
        
        
                

        