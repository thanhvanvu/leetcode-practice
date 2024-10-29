# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/
# https://www.youtube.com/watch?v=ZHjKhUjcsaU

def replaceElements_bruteForce(arr):
    for n in range(len(arr)):
        greatest = 0
        k = n + 1
        if k == len(arr):
            arr[n] = -1
            return arr
        while k < len(arr):
            greatest = max(arr[k], greatest)
            k += 1

        arr[n] = greatest


def replaceElements(arr):
    # initial max base case = -1
    # reverse loop
    # new max = max(oldMax, arr[i])

    rightMax = -1
    for i in range(len(arr) - 1, -1, -1):
        newMax = max(arr[i], rightMax)
        arr[i] = rightMax
        rightMax = newMax

    return arr


array = [17, 18, 5, 4, 6, 1]
print(replaceElements(array))
