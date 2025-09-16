class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_que = deque()
        max_que = deque()
        left = 0
        answer = 0
        for i,num in enumerate(nums):
            while min_que and min_que[-1]>num:
                min_que.pop()
            min_que.append(num)
            while max_que and max_que[-1]<num:
                max_que.pop()
            max_que.append(num)
            while abs(max_que[0]-min_que[0])>limit:
                if min_que[0]==nums[left]:
                    min_que.popleft()
                if max_que[0] == nums[left]:
                    max_que.popleft()
                left+=1
            answer = max(answer,i-left+1)
        return answer




        