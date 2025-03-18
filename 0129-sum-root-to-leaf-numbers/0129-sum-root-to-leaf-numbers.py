# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, temp):
            if node is None:
                return 0
            temp = temp * 10 + node.val
            if not node.left and not node.right:  
                return temp
            return dfs(node.left, temp) + dfs(node.right, temp)
        
        return dfs(root, 0)

        