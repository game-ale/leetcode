# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs (node):
            if node is None:
                return 
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)
            return nums
        def tree(low , high):
            if low > high:
                return None
            mid = (low + high)//2
            left = tree(low,mid-1)
            right = tree(mid+1,high)
            ans = TreeNode(nums[mid],left,right)
            return ans
        nums = []
        dfs(root)
        return tree(0,len(nums)-1)
        