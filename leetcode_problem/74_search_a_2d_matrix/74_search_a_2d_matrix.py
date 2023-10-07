# https://leetcode.com/problems/search-a-2d-matrix/description/
# https://www.youtube.com/watch?v=Ber2pi2C0j0

def searchMatrix(matrix, target):
    top = 0
    bottom = len(matrix) - 1

    while top <= bottom:
        # after checking
        # midRow is the row that contain the target
        midRow = (bottom + top) // 2

        if target < matrix[midRow][0]:
            bottom = midRow - 1

        elif target > matrix[midRow][-1]:
            top = midRow + 1

        else:
            break

    # top, bottom are from the while loop after checking
    row = (bottom + top) // 2

    # run binary search from the row
    l = 0
    r = len(matrix[row]) - 1
    while l < r:
        m = (r + l) // 2

        if target < matrix[row][m]:
            r = m - 1
        elif target > matrix[row][m]:
            l = m + 1
        else:
            # if we find target, return True
            return True

    # if target not found, return False
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13

print(searchMatrix(matrix, target))
