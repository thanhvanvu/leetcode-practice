# https://www.youtube.com/watch?v=68isPRHgcFQ
# https://leetcode.com/problems/concatenation-of-array/submissions/

def getConcatenation(arr):
    for i in range(len(arr)):

        arr.append(arr[i])
    return arr


if __name__ == '__main__':
    myArray = [1, 2, 1]
    length_arr = len(myArray)

    a = getConcatenation(myArray)

    print('remove duplicate', a, myArray)
