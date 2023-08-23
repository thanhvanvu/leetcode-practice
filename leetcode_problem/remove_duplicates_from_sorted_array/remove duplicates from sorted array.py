# https://www.youtube.com/watch?v=DEJAZBq0FDA&t=4s
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(arr):
    # set left pointer
    # no need to check index 0
    left_pointer = 1

    for right_pointer in range(1, len(arr)):
        # check if current element is different than last element
        if arr[right_pointer] != arr[right_pointer - 1]:
            arr[left_pointer] = arr[right_pointer]
            left_pointer += 1

    return left_pointer


if __name__ == '__main__':
    myArray = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    length_arr = len(myArray)

    a = removeDuplicates(myArray)

    print('remove duplicate', a, myArray)
