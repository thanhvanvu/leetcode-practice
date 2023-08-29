# https://www.youtube.com/watch?v=KLlXCFG5TnA&t=24s
# https://leetcode.com/problems/two-sum/

def twoSum(arr, target):
    hashMap = []
    result = 0

    # loop thru every element in list
    for i in range(len(arr)):
        # get result
        # ex: 6-3 = 2
        result = target - arr[i]

        # if 2 is not in hashMap ==> append 2 to hashMap
        if result not in hashMap:
            hashMap.append(arr[i])
        else:

            # hashMap = [2]
            # result = 6-4 = 2. 2 is in hashMap ==> return
            return [arr.index(result), i]


def twoSumBruteForce(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]


if __name__ == '__main__':
    array = [3, 2, 4]
    length_arr = len(array)

    print(twoSumBruteForce(array, 6))
