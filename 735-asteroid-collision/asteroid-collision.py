class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            while stack and stack[-1] > 0 and asteroids[i] < 0 and stack[-1] < -asteroids[i]:
                stack.pop()
            
            if stack and stack[-1] > 0 and asteroids[i] < 0:
                if stack[-1] == -asteroids[i]:
                    stack.pop()
            else:
                stack.append(asteroids[i])
        return stack
        
        