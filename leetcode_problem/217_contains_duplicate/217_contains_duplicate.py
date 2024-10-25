def containsDuplicate(nums):
    # create hash set
    hashSet = set()

    # loop through all element
    for value in nums:

        # value = 1
        # hashSet = {1}

        # value = 2
        # hashSet = {1, 2}

        # value = 2
        # hashSet has 2 ==> return True
        if value not in hashSet:
            hashSet.add(value)
        else:
            return True

    return False


def containsDuplicate2(nums):
    hashSet = set()

    # loop through all element
    for value in nums:
        if value not in hashSet:
            hashSet.add(value)
        else:
            return True  # found duplicated -> return True

    # if for loop is done, it means no duplcated -> return False
    return False


array = [1, 2, 3, 3]
print(containsDuplicate2(array))
