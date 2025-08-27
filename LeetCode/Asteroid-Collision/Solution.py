class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []

        for asteroid in asteroids:
            alive = True
            while stk and asteroid < 0 < stk[-1]:
                if abs(asteroid) > abs(stk[-1]):
                    stk.pop() 
                    continue
                elif abs(asteroid) == abs(stk[-1]):
                    stk.pop() 
                alive = False
                break
            if alive:
                stk.append(asteroid)

        return stk
