class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        sum_even = sum(element for element in nums if element%2==0)
        for querie in queries:
            if nums[querie[1]]%2==0:
                sum_even -=nums[querie[1]]
            nums[querie[1]]=querie[0]+nums[querie[1]]
            if nums[querie[1]]%2==0:
                sum_even +=nums[querie[1]]
            answer.append(sum_even)
        return answer


        