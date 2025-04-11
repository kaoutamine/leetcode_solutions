class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid < 0:
                #asteroid goes left
                destroyed = False
                while stack and stack[-1] > 0:
                    abs_curr, abs_left = abs(asteroid), abs(stack[-1])
                    if abs_curr == abs_left:
                        stack.pop()
                        destroyed = True
                        break
                    elif abs_curr > abs_left:
                        stack.pop()
                        continue
                    else:
                        destroyed = True
                        break
                if not destroyed:
                    stack.append(asteroid)
            else:
                stack.append(asteroid)
        
        return stack

                



        