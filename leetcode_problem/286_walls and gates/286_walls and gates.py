# https://www.youtube.com/watch?v=e69C6xhiSQE&ab_channel=NeetCode
from collections import deque


def wallsAndGates(rooms):
    ROWS = len(rooms)
    COLS = len(rooms[0])
    q = deque()
    visit = set()
    GATE = 0
    BLOCK = -1
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def addRoom(r, c):
        # if out of bound
        # or already visited
        # or see the block --> return and try different path
        if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or rooms[r][c] == BLOCK:
            return

        # if we see empty path
        visit.add((r, c))

        # append those path to q
        q.append([r, c])

    for i in range(ROWS):
        for j in range(COLS):
            if rooms[i][j] == GATE:
                q.append([i, j])
                visit.add((i, j))
    dist = 0

    while q:
        for i in range(len(q)):
            row, col = q.popleft()
            rooms[row][col] = dist

            addRoom(row, col + 1)
            addRoom(row + 1, col)
            addRoom(row, col - 1)
            addRoom(row - 1, col)

        # increase distance by 1 after looping every layer
        dist += 1

    print(rooms)


def wallsAndGates_practice(rooms):
    ROWS = len(rooms)
    COLS = len(rooms[0])
    q = deque()
    visit = set()
    GATE = 0
    BLOCK = -1
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for i in range(ROWS):
        for j in range(COLS):
            if rooms[i][j] == GATE:
                q.append([i, j])
                visit.add((i, j))
    dist = 0

    while q:
        for i in range(len(q)):
            row, col = q.popleft()
            rooms[row][col] = dist

            for dr, dc in direction:
                new_row = row + dr
                new_col = col + dc

                if new_row < 0 or new_col < 0 or new_row >= ROWS or new_col >= COLS or (new_row, new_col) in visit or rooms[new_row][new_col] == BLOCK:
                    continue

                visit.add((new_row, new_col))
                q.append([new_row, new_col])

        # increase distance by 1 after looping every layer
        dist += 1

    print(rooms)


matrix = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1],
          [0, -1, 2147483647, 2147483647]]
print(wallsAndGates_practice(matrix))
