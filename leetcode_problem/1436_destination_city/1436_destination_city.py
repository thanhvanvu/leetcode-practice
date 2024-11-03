# https://leetcode.com/problems/destination-city/description/
# https://www.youtube.com/watch?v=Hi8vMnnTZHE

def destCity(paths):
    # [["B","C"],["D","B"],["C","A"]]
    # result = "D" -> "B" -> "C" -> "A"
    # put start path to the SET
    # check the end path if it is in the SET ? -> No -> it is the destination

    startSet = set()

    # put start path in SET
    for path in paths:
        startPath = path[0]
        startSet.add(startPath)

    # check end path in SET or not ?
    for path in paths:
        endPath = path[1]
        if endPath not in startSet:
            return endPath


lst = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]

print(destCity(lst))
