# https://www.youtube.com/watch?v=y704fEOx0s0&ab_channel=NeetCode
# https://leetcode.com/problems/rotting-oranges/description/

from collections import deque


def orangesRotting(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    visit = set()
    q = deque()
    fresh = 0
    time = 0
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    # count # of fresh orange
    # add rotten orange in queue
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1:
                fresh += 1

            if grid[i][j] == 2:
                q.append([i, j])
                visit.add((i, j))

    # if we do not add condition fresh > 0
    # while loop will execute one more time
    # leading time += 1 --> wrong
    # so we want to stop if fresh = 0
    while q and fresh > 0:
        for _ in range(len(q)):
            row, col = q.popleft()

            for dr, dc in direction:
                n_row = row + dr
                n_col = col + dc

                if n_row < 0 or n_col < 0 or n_row >= ROWS or n_col >= COLS or (n_row, n_col) in visit or grid[n_row][
                    n_col] == 0:
                    continue

                visit.add((n_row, n_col))
                grid[n_row][n_col] = 2

                q.append([n_row, n_col])
                fresh -= 1
        time += 1

    if fresh == 0:
        return time
    else:
        return -1


matrix = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
print(orangesRotting(matrix))
