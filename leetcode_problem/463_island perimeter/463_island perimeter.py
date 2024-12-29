# https://leetcode.com/problems/island-perimeter/description/
# https://www.youtube.com/watch?v=fISIuAFRM2s&ab_channel=NeetCode

def islandPerimeter(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    visit = set()

    def dfs(row, col):
        # if out of bound, or we see the water
        # return 1
        if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0:
            return 1

        # if we already visited the land
        # return 0
        if (row, col) in visit:
            return 0

        visit.add((row, col))

        right = dfs(row, col + 1)
        down = dfs(row + 1, col)
        left = dfs(row, col - 1)
        up = dfs(row - 1, col)

        perimeter = (right + down + left + up)

        return perimeter

    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1:
                return dfs(i, j)

    return 0


matrix = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]

# idea:
# use for loop to loop through the matrix
# if we see 1, run dfs for 4 direction to check
# if direction is out of bound, or water, return 1
# add that node to set()
# if we go to that node again, just return 0
# after run dfs(), keep track "1" and run dfs again

print(islandPerimeter(matrix))
