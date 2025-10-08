class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        n = len(potions)
        
        def binary( l, r, arr, val):
            if l>r:
                return l
            mid = (l+r)//2
            if val*arr[mid]>=success:
                return (binary(l, mid-1,arr, val ))
            else:
                return(binary(mid+1, r, arr, val))


        for num in spells:
            l , r = 0, n - 1
            temp = binary(l,r, potions, num)
            val = n-temp
            ans.append(val)
        return ans


        