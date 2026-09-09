class Solution(object):
    def countCommas(self, n):
        current = 1000
        answer = 0
        while current <=n:
            answer +=(n-current+1)
            current*=1000
        return answer

        