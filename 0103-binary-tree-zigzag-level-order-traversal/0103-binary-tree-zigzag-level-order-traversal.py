# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stk = deque([root])
        ans = []
        odd = True
        while stk:
            level = []
            for v in range(0,len(stk)):
                top = stk.popleft()
                if top is None :
                    continue
                level.append(top.val)
                stk.append(top.left)
                stk.append(top.right)
            if level:
                if odd:
                    ans.append(level)
                else:
                    ans.append(level[::-1])
            odd = not odd
        return ans
        