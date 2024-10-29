# https://www.youtube.com/watch?v=KLlXCFG5TnA&t=24s
# https://leetcode.com/problems/two-sum/

def twoSum(arr, target):
    hashMap = dict()  # {val: index}
    result = 0

    # loop thru every element in list
    for i in range(len(arr)):
        # get result
        # ex: 6-3 = 2
        # ex: 6-2 = 4
        value = arr[i]
        diff = target - value

        # if 2 is not in hashMap ==> append 3 to hashMap
        # if 4 is not in hashmap ==> append 2 to hashMap
        if diff not in hashMap:
            hashMap[value] = i  # {3: 0, 2: 1}
        else:

            # hashMap = {3: 0, 2: 1}
            # result = 6-4 = 2. 2 is in hashMap ==> return
            return [hashMap[diff], i]


def twoSumBruteForce(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]


def twoSumPractice(arr, target):
    hashMap = {}  # store {value: i}
    result = 0

    for i in range(len(arr)):
        value = arr[i]
        result = target - value

        if result not in hashMap:
            hashMap[value] = i
        else:
            return [hashMap[result], i]


if __name__ == '__main__':
    array = [3, 2, 4]
    length_arr = len(array)

    print(twoSumPractice(array, 5))
