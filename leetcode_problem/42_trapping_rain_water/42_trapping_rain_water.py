# https://leetcode.com/problems/trapping-rain-water/description/
# https://www.youtube.com/watch?v=ZI2z5pq0TqA

# prefix, postfix
def trap(height):
    L = 1
    R = len(height) - 2
    max_left_array = [0 for i in range(len(height))]
    max_right_array = [0 for i in range(len(height))]

    # calculate maximum prefix, postfix
    # [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
    # [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0]
    m_left = float("-inf")
    m_right = float("-inf")
    while L < len(height) and R >= 0:
        m_left = max(height[L - 1], m_left)
        max_left_array[L] = m_left

        m_right = max(height[R + 1], m_right)
        max_right_array[R] = m_right

        L += 1
        R -= 1

    # find min(left, right) for every element
    # based on 2 array
    # [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
    # [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0]
    # [0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0] <- min

    # also calculate min(left, right) - height(i)
    # if < 0 -> round to 0
    # [0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0] <- min
    # [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # [0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0]

    # calculate total trapped rain.

    min_height = float("-inf")
    total_trapped_rain = 0
    for i in range(len(height)):
        min_height = min(max_left_array[i], max_right_array[i])  # <- find min height
        trapped_rain = 0 if min_height - height[i] < 0 else min_height - height[i]  # calculate trapped rain
        total_trapped_rain += trapped_rain  # calculate total trapped rain

    return total_trapped_rain


def trap_2pointer(height):
    L = 0
    R = len(height) - 1

    max_left = height[L]
    max_right = height[R]

    total_trapped_rain = 0

    while L < R:
        if max_left <= max_right:
            trapped_rain = 0 if max_left - height[L] <= 0 else max_left - height[L]
            total_trapped_rain += trapped_rain

            # update max left
            L += 1
            max_left = max(max_left, height[L])

        else:
            trapped_rain = 0 if max_right - height[R] <= 0 else max_right - height[R]
            total_trapped_rain += trapped_rain

            # update max right
            R -= 1
            max_right = max(max_right, height[R])

    return total_trapped_rain


h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(trap_2pointer(h))
