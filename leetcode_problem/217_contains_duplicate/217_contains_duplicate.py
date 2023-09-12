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


array = [1, 2, 3, 4]
print(containsDuplicate(array))
