# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = []
        if root is None:
            return 0
        def progress(root , bit = ""):
            if root is None:   
                return
            if root.left is None  and root.right is None:
                bit = bit+str(root.val)
                ans.append(bit)
                return 
            bit = bit+str(root.val)
            progress(root.left , bit)
            progress(root.right , bit)
        progress(root, "")
        res = 0
        for num in ans:
            temp = int(num , 2)
            res += temp
        return res

        
        