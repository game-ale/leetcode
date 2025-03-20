# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node,p,q):
            if not node or node.val == p.val or node.val == q.val:
                return node
            left = dfs(node.left,p,q)
            right = dfs(node.right,p,q)
            if left and right:
                return node
            else:
                return left if left else right
        return(dfs(root,p,q))
        