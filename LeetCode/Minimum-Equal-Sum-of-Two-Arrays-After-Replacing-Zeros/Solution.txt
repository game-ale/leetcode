
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        cntz1, cntz2 = nums1.count(0), nums2.count(0)
        new_sum1 = sum1 + cntz1
        new_sum2 = sum2 + cntz2
        if new_sum1 == new_sum2:
            return new_sum1
        elif cntz1 == 0 and new_sum1 < new_sum2:
            return -1
        elif cntz2 == 0 and new_sum2 < new_sum1:
            return -1
        else:
            return max(new_sum1, new_sum2)
