class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)<=2:
            return s
        stk = [s[0],s[1]]
        for char in s[2:]:
            if char == stk[-1] and char == stk[-2]:
                continue
            stk.append(char)
        return "".join(stk)
        