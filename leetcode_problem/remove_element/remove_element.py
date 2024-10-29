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


def removeElement_practice(nums, val):
    k = 0

    for i in range(len(nums)):
        # if nums[i] != val:
        #     nums[k] = nums[i]
        #     k += 1

        # if we see nums[i] == val
        # do not increase k, increase i until we found nums[i] = val

        if nums[i] == val:
            continue
        else:
            # at position k, replace nums[k] with nums[i] we just found,
            # so the val at position k is replaced and get rid of.
            nums[k] = nums[i]
            k += 1

    return k


if __name__ == '__main__':
    myArray = [3, 2, 2, 3]
    print(removeElement_practice(myArray, 3))
