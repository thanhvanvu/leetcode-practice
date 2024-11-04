# https://leetcode.com/problems/path-crossing/description/
# https://www.youtube.com/watch?v=VWRJBNP7uH8
def isPathCrossing(path):
    direction = {
        "N": [0, 1],
        "S": [0, -1],
        "E": [1, 0],
        "W": [-1, 0]
    }

    # create set, we store every path in set
    # if we see path is already in set
    # it means we cross it --> return true
    isCrossed = set()
    isCrossed.add((0, 0))

    x, y = 0, 0

    # (0, 0)
    # N -> (0 + 0, 0 + 1) = (0, 1)
    # E -> (0 + 1, 1 + 0) = (1, 1)
    # S -> (1 + 0, 1 + -1 ) = (1, 0)
    # ...
    for i in path:
        x = x + direction[i][0]
        y = y + direction[i][1]
        origin = (x, y)
        if origin in isCrossed:
            return True
        else:
            isCrossed.add(origin)

    return False


path = "NESWW"
print(isPathCrossing(path))
