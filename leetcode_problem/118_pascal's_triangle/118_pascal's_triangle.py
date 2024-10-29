# https://leetcode.com/problems/pascals-triangle/description/
# https://www.youtube.com/watch?v=nPVEaB3AjUM


def generate(numRows: int):
    output = [[1]]

    for i in range(numRows-1):
        newRow = ([0] + output[i] + [0])
        result = []
        for j in range(len(newRow)-1):
            result.append(newRow[j] + newRow[j+1])

        output.append(result)
    return output

# output = [[1], [1,1], [1,2,1]]

# newRow = [0] + [1,2,1] + [0]  => [0,1,2,1,0]
# calculate the sum =>  result = [1,3,3,1]
# add result to output => [[1], [1,1], [1,2,1], [1,3,3,1]]

# newRow = [0] + [1,3,3,1] + [0]  => [0,1,3,3,1,0]
# calculate the sum =>  result = [1,4,6,4,1]
# add result to output => [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]

print(generate(5))
