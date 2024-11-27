# https://leetcode.com/problems/asteroid-collision/description/
# https://www.youtube.com/watch?v=LN7KjRszjk4

def asteroidCollision(asteroids):
    stack = []

    for num in asteroids:
        # condition that collision happens:
        # stack must have element (len stack !=0 )
        # current num must be < 0
        # top stack must be > 0
        while stack and num < 0 and stack[-1] > 0:
            if stack[-1] > abs(num):
                num = 0  # important: set num = 0 to break while loop
            elif stack[-1] == abs(num):
                num = 0
                stack.pop()
            else:
                stack.pop()

        # if num != 0: append
        # because num = 0 was set above
        # num will not be added to stack
        if num:
            stack.append(num)

    return stack


asteroids = [-2, -2, 1, -2]
print(asteroidCollision(asteroids))
