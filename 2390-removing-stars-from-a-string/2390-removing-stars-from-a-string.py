class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char=="*":
                stack.pop()
            else:
                stack.append(char)
        # ans = ""
        # for c in stack:
        #     ans+=c


        
        return "".join(stack)
