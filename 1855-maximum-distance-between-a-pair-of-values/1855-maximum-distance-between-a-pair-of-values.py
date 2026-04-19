from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        def find_farthest(nums2, i, val):
            left, right = i, len(nums2) - 1
            ans = i
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums2[mid] >= val:
                    ans = mid       # valid, try to go further right
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return ans
        
        res = 0
        
        for i in range(len(nums1)):
            j = find_farthest(nums2, i, nums1[i])
            res = max(res, j - i)
            
        return res