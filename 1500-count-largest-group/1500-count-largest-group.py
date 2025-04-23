class Solution:
    def countLargestGroup(self, n: int) -> int:
        cnt = defaultdict(list)
        for i in range(1, n + 1):
            digit_sum = sum(int(digit) for digit in str(i))
            cnt[digit_sum].append(i)
        max_size = max(len(group) for group in cnt.values())
        return sum(1 for group in cnt.values() if len(group) == max_size)
        

            
        
        
        