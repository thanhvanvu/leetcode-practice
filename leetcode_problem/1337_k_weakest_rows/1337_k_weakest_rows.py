# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/


def kWeakestRows(mat, k):
    result = []

    # count 1
    # overwrite the row
    # [1, 0, 0, 0] => [count, index]
    for i in range(len(mat)):
        count = mat[i].count(1)
        mat[i] = [count, i]

    # sort by count first
    # if count is the same, sort by index
    mat = sorted(mat, key=lambda x: (x[0], x[1]))

    # append the index to result
    for i in range(0, k):
        result.append(mat[i][1])

    return result


mat = [[1, 0, 0, 0],
       [1, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 0]]
k = 3

print(kWeakestRows(mat, 2))
