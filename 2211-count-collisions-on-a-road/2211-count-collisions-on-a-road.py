class Solution:
    def countCollisions(self, directions: str) -> int:
        res = 0
        flag = -1

        for c in directions:
            if c == "L":
                if flag >= 0:
                    res += flag + 1
                    flag = 0
            elif c == "S":
                if flag > 0:
                    res += flag
                flag = 0
            else:
                if flag >= 0:
                    flag += 1
                else:
                    flag = 1
        return res