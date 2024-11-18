# https://leetcode.com/problems/container-with-most-water/description/
# https://www.youtube.com/watch?v=UuiTKBwPgAo

def maxArea_brute_force(height):
    area = 0
    max = 0

    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            width = j - i

            if height[i] <= height[j]:
                area = height[i] * width
            elif height[i] >= height[j]:
                area = height[j] * width

            if area >= max:
                max = area

    return max

def maxArea(height):
    area = 0
    max = 0

    l = 0
    r = len(height) - 1

    while l < r:
        width = r - l
        area = min(height[l], height[r]) * width

        if area >= max:
            max = area

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max


# two pointer
def maxArea_practice(height):
    L = 0
    R = len(height) - 1
    result_max_area = float("-inf")

    while L < R:
        width = R - L
        h = min(height[L], height[R])
        area = width * h

        result_max_area = max(result_max_area, area)

        if height[L] <= height[R]:
            L += 1
        else:
            R -= 1

    return result_max_area



h = [1,1]

print(maxArea_practice(h))
