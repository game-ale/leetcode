class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        st = {"(", "[", "{"}
        dc = {")":"(","]":"[", "}":"{"}
        for char in s:
            if char in dc:
                if not stack or stack[-1]!=dc[char]:
                    return False
                stack.pop()
            elif char in st:
                stack.append(char)
            # print(stack)
        if stack:
            return False
        return True 



    