class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        
        par = []
        rank = [1] * len(nums)

        for i in range(len(nums)):
            par.append(i)
        

        def find(node):

            while node != par[node]:
                node = par[node]
            
            return node
        
        def union(nd1, nd2):

            n1 = find(nd1)
            n2 = find(nd2)

            if n1 == n2:
                return True
            
            if rank[n2] > rank[n1]:
                rank[n2] += rank[n1]
                par[n1] = n2
                rank[n1] = 0
            else:
                rank[n1] += rank[n2]
                par[n2] = n1
                rank[n2] = 0

            return False

        i = 0
        j = 1

        while j < len(nums):

            if nums[j] - nums[i] <= maxDiff:
                union(i, j)
                i += 1
                j += 1
            else:
                i = j
                j += 1

        ans = []
        for i, j in queries:
            n1 = find(i)
            n2 = find(j)
            if (n1 == n2):
                ans.append(True)
            else:
                ans.append(False)
        
        return ans