class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum_num , product_num = 0 , 1
        x = n
        while n:
            digit = n%10
            n = n//10
            sum_num = sum_num +digit
            product_num = product_num*digit
        total_sum = sum_num + product_num
        if total_sum and x%total_sum:
            return False
        else:
            return True

        