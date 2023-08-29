# https://www.youtube.com/watch?v=Pcd1ii9P9ZI
# https://leetcode.com/problems/remove-element/
def removeElement(arr, value):
    # set flag
    flag = 0

    for i in range(0, len(arr)):
        if arr[i] != value:
            arr[flag] = arr[i]
            flag += 1
    return flag


if __name__ == '__main__':
    myArray = [0, 1, 2, 2, 3, 0, 4, 2]
    length_arr = len(myArray)

    a = removeElement(myArray, 2)

    print('remove duplicate', a, myArray)
