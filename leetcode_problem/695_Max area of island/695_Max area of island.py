# https://leetcode.com/problems/max-area-of-island/description/
# https://www.youtube.com/watch?v=iJGr1OtmH0c&ab_channel=NeetCode

def maxAreaOfIsland(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    max_area = 0

    def dfs(row, col):
        # Base case: if out of bounds or at a water cell, return 0
        if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0:
            return 0

        # Mark the current cell as visited
        grid[row][col] = 0

        # Initialize area for the current cell
        area = 1

        area += dfs(row, col + 1)  # right
        area += dfs(row + 1, col)  # down
        area += dfs(row, col - 1)  # left
        area += dfs(row - 1, col)  # up

        return area

    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(i, j))

    return max_area


matrix = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
          [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

print(maxAreaOfIsland(matrix))
