# https://leetcode.com/problems/find-the-town-judge/description/
# https://www.youtube.com/watch?v=QiGaxdUINJ8&ab_channel=NeetCodeIO
from collections import defaultdict


def findJudge(trust, n):
    incoming = defaultdict(int)
    outgoing = defaultdict(int)

    # count number of incoming and outgoing edge
    # and put in hashmap
    for x, y in trust:
        if x not in outgoing:
            outgoing[x] = 1
        else:
            outgoing[x] += 1

        if y not in incoming:
            incoming[y] = 1
        else:
            incoming[y] += 1

    # the judge will be satisfied
    # if that number has 0 outgoing edge
    # and that number = n - 1
    for i in range(1, n+1):
        if outgoing[i] == 0 and incoming[i] == n-1:
            return i

    # if for loop is done, cant find the judge
    return -1


matrix = [[1, 3], [2, 3]]

print(findJudge(matrix, 3))
