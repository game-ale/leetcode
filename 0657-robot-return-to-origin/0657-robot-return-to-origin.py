class Solution:
    def judgeCircle(self, moves: str) -> bool:
        u = moves.count("U")
        d = moves.count("D")
        r = moves.count("R")
        l = moves.count("L")
        return (u==d and r==l)
        