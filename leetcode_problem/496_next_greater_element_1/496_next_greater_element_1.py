# O(n.m)
def nextGreaterElement(nums1, nums2):
    # value in nums1 will be always in nums2
    # store value and index of every element in nums1 to hashtable
    # in nums2, check every element to see if that element is in hashTable ?
    # if yes, check element + 1

    hashNums1 = {}
    output = [0] * len(nums1)

    for i, value in enumerate(nums1):
        hashNums1[value] = i

    for i, value in enumerate(nums2):

        # check if element in hashNums1 ?
        # if yes, check all elements behind that element
        # if we see the NEW element > OlD element
        # append it to [output] and break for loop
        if value in hashNums1:
            if i + 1 >= len(nums2):
                output[hashNums1[value]] = -1
                break

            for j in range(i + 1, len(nums2)):
                if nums2[j] > value:
                    output[hashNums1[value]] = nums2[j]
                    break
                else:
                    output[hashNums1[value]] = -1

    return output


def nextGreaterElement_stack(nums1, nums2):
    hashNums1 = {}
    stack = []
    output = [-1] * len(nums1)

    for i, value in enumerate(nums1):
        hashNums1[value] = i

    for i in range(len(nums2)):
        current = nums2[i]
        while stack and current > stack[-1]:
            valueStack = stack.pop()
            index = hashNums1[valueStack]

            output[index] = current

        if current in hashNums1:
            stack.append(current)

    return output


def nextGreaterElement_practice(nums1, nums2):
    hashNums1 = {}
    output = [0] * len(nums1)

    for i, value in enumerate(nums1):
        hashNums1[value] = i

    for i, value in enumerate(nums2):
        if value in hashNums1:
            if i + 1 >= len(nums2):
                output[hashNums1[value]] = -1

            for j in range(i + 1, len(nums2)):
                if nums2[j] > value:
                    output[hashNums1[value]] = nums2[j]
                    break
                else:
                    output[hashNums1[value]] = -1

    print(output)


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

print(nextGreaterElement_practice(nums1, nums2))
