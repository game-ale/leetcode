class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(nums,left,right):
            if left >= right:
                return 
            mid = (right + left)//2
            mergesort(nums,left,mid)
            mergesort(nums,mid+1,right)
            return (merge(nums,left,mid,right))
        def merge (nums,left, mid ,right):
            i, j = left, mid+1
            temp = []
            while i <= mid and j <= right:
                if nums[i]<=nums[j]:
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    j+=1
            while i <= mid:
                temp.append(nums[i])
                i+=1
            while j <= right:
                temp.append(nums[j])
                j+=1
            nums[left:right+1] = temp
            
        mergesort(nums,0,len(nums)-1)
        return (nums)
        



        