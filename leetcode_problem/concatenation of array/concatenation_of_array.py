# https://www.youtube.com/watch?v=68isPRHgcFQ
# https://leetcode.com/problems/concatenation-of-array/submissions/

def getConcatenation(arr):
    for i in range(len(arr)):
        arr.append(arr[i])
    return arr


def getConcatenation2(nums):
    result = []

    for i in range(2):
        for num in range(len(nums)):
            result.append(nums[num])

    return result


if __name__ == '__main__':
    myArray = [1, 2, 1]
    print(getConcatenation2(myArray))
