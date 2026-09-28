class Solution:
    def maxDepth(self, s: str) -> int:
        stk = []
        ans = 0
        for char in s:
            if stk and char == ')':
                ans = max(len(stk),ans)
                stk.pop()
            elif char == '(':
                stk.append(char)
        return ans
                

        