# https://leetcode.com/problems/sqrtx/description/
# https://www.youtube.com/watch?v=zdMhGxRWutQ&t=467s

def mySqrt(x):
    L = 0
    R = x
    result = 0

    while L <= R:
        mid = L + (R - L) // 2
        square = mid * mid

        if square > x:
            # find smaller number
            R = mid - 1
        else:
            L = mid + 1

            # result could be 3, 4, 5
            # we want to get the result that ^2 closet to x
            result = max(mid, result)

    return result


x = 8

print(mySqrt(x))
