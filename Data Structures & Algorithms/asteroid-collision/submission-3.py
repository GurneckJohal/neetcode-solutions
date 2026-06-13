class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            asteroid_destroyed = False
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    asteroid_destroyed = True
                    break
                else:
                    asteroid_destroyed = True
                    break
            if not asteroid_destroyed:
                stack.append(asteroid)
            
        
        return stack