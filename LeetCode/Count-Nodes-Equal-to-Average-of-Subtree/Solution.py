# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return (0, 0, 0)

            left_sum, left_count, left_match = dfs(node.left)
            right_sum, right_count, right_match = dfs(node.right)

            curr_sum = left_sum + right_sum + node.val
            curr_count = left_count + right_count + 1
            match = left_match + right_match

            if node.val == curr_sum // curr_count:
                match += 1

            return (curr_sum, curr_count, match)

        return dfs(root)[2]

        