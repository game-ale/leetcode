class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArray = nums1 + nums2
        mergedArray.sort()
        midLength = int(len(mergedArray) / 2)
        if (len(mergedArray) % 2 == 0): # if its even
            return (mergedArray[midLength-1] + mergedArray[midLength] ) / 2
        else: # if its odd
            return mergedArray[midLength]