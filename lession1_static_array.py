# Press Shift+F10 to execute it or replace it with your code.

# Remove from the last position in the array if the array is not empty
def removeEnd(arr, length):
    if length > 0:
        # overwrite the last element with some default value
        # length = 5 ==> last element = 5-1 = 4
        arr[length - 1] = 0


# remove value at index i before shifting elements to the left
def removeMiddle(arr, i, length):
    # shift starting from i + 1 to end
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]


if __name__ == '__main__':
    myArray = [4, 5, 6]
    length_arr = len(myArray)
    print(myArray)
    removeEnd(myArray, length_arr)
    print('remove last element', myArray)

    myArray2 = [5, 9, 10]
    len_myArray2 = len(myArray2)
    print(myArray2)
    removeMiddle(myArray2, 1, len_myArray2)
    print('remove middle element', myArray2)
