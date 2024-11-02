def getRow(rowIndex):
    output = [[1]]

    # print rowIndex
    # loop through rowIndex + 1
    for i in range(1, rowIndex + 1):
        last_row = output[-1]
        temp_row = [0] + last_row + [0]
        row = []
        val = 0

        # len(num) - 1 because we use i and i + 1
        # if len(num) --> out of bound
        for j in range(len(temp_row) - 1):
            val = temp_row[j] + temp_row[j + 1]
            row.append(val)
        output.append(row)

    return output[-1]


print(getRow(1))
