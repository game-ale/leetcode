class Solution:
    def merge(self, nums_1: List[int], m: int, nums_2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums_1 in-place instead.
        """
          

        i, j, k = m - 1, n - 1, m + n - 1  # Pointers for nums_1, nums_2, and merged array

        while j >= 0: 

            if i >= 0 and nums_1[i] > nums_2[j]:

                nums_1[k] = nums_1[i]

                i -= 1

            else:

                nums_1[k] = nums_2[j]

                j -= 1

            k -= 1