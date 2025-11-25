class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        ans  = 0
        for len_k in range(1,k+1):
            ans = (ans*10+1)%k
            if ans%k==0:
                return len_k
        return -1 