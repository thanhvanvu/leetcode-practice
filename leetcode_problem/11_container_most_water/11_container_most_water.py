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


h = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(maxArea(h))
