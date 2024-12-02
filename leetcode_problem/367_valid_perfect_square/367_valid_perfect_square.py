# https://leetcode.com/problems/valid-perfect-square/description/
#

def isPerfectSquare(num):
    L = 0
    R = num

    while L <= R:
        mid = L + (R-L) // 2
        square = mid ** 2

        if square > num:
            R = mid - 1
        elif square < num:
            L = mid + 1
        else:
            return True

    return False


num = 14

print(isPerfectSquare(num))