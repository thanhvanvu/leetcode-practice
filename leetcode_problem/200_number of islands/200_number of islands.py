# https://leetcode.com/problems/number-of-islands/description/
# https://www.youtube.com/watch?v=gCswsDauXPc&ab_channel=GregHogg

def numIslands(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    islands = 0

    def dfs(row, col):
        # base case
        # if you go out of bound or "0", return to continue dfs()
        if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == "0":
            return

        # if we see 1, mark "1" to "0":
        grid[row][col] = "0"

        # go 4 direction
        dfs(row, col + 1)  # right
        dfs(row + 1, col)  # down
        dfs(row, col - 1)  # left
        dfs(row - 1, col)  # up

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == "1":
                dfs(row, col)
                islands += 1

    return islands


matrix = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

# idea:
# use for loop to loop through the matrix
# if we see "1", run dfs() 4 direction to mark all "1" to "0"
# [
#   ["0","0","0","0","0"],
#   ["0","0","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# after run dfs(), keep track "1" and run dfs again

print(numIslands(matrix))
