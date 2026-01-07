class Solution:
    def maxProduct(self, root):
        MOD = 10**9 + 7
        self.maxProduct = 0

        def dfs_sum(node):
            if not node:
                return 0
            return node.val + dfs_sum(node.left) + dfs_sum(node.right)

        totalSum = dfs_sum(root)

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            sub = node.val + left + right
            self.maxProduct = max(self.maxProduct, sub * (totalSum - sub))
            return sub

        dfs(root)
        return self.maxProduct % MOD