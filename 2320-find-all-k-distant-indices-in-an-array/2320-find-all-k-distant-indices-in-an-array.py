class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        cnt = defaultdict(int)
        stop = 0
        ans = []
        for i,num in enumerate(nums):
            if num == key:
                x,y = max(i-k,stop),min(len(nums),i+k+1)
                ans.extend([j for j in range(x,y)])
                stop = y
        return ans
               




        