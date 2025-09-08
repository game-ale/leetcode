
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return
        pivot_val = random.choice(nums)
        left =  [x for x in nums if x > pivot_val]
        mid  =  [x for x in nums if x == pivot_val]
        right = [x for x in nums if x < pivot_val]
        
        Low, Middle = len(left), len(mid)
        
        if k <= Low:
            return self.findKthLargest(left, k)
        elif k > Low + Middle:
            return self.findKthLargest(right, k - Low - Middle)
        else:
            return mid[0]