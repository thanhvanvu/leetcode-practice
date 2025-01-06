# https://www.youtube.com/watch?v=e69C6xhiSQE&ab_channel=NeetCode
from collections import deque


def countSubIslands(grid1, grid2):
    ROWS = len(grid1)
    COLS = len(grid2)
    visit = set()
    count = 0

    def dfs(row, col):
        if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid2[row][col] == 0 or (row, col) in visit:
            return True

        visit.add((row, col))
        res = True
        if grid1[row][col] == 0:
            return False

        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)

        return res

    for i in range(ROWS):
        for j in range(COLS):
            if grid2[i][j] == 1 and (i, j) not in visit:
                if dfs(i, j):
                    count += 1
    return count


matrix = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]]
matrix2 = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
print(countSubIslands(matrix, matrix2))
