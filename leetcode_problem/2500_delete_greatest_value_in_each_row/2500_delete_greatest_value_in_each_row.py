# https://leetcode.com/problems/delete-greatest-value-in-each-row/description/

def deleteGreatestValue(grid):
    length = len(grid[0])
    result = 0

    # loop through until column = 0
    while length > 0:
        maximum = 0
        for i in grid:
            # sort array
            i.sort()

            # get maximum value
            maximum = max(maximum, i[-1])

            # pop that value from the array
            i.pop()

        # calculate result
        result += maximum

        length -= 1

    return result

grid = [[10]]
print(deleteGreatestValue(grid))
