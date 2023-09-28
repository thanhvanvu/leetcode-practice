# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

def findRestaurant(list1, list2):
    hashMap = {}
    j = 0
    bucket = [[] for i in range(len(list1) + len(list2))]

    # store list1 into hashMap {"shogun": 0, "KFC": 1}
    for i in range(len(list1)):
        hashMap[list1[i]] = i

    # loop through list2
    while j < len(list2):
        # if word is in hashMap
        # calculate sum i + j
        # store that into bucket
        if list2[j] in hashMap:
            sumIndex = hashMap[list2[j]] + j
            bucket[sumIndex].append(list2[j])
        j += 1

    # loop through bucket and return first element
    for i in range(len(bucket)):
        if len(bucket[i]) == 0:
            continue
        else:
            return bucket[i]







list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]

print(findRestaurant(list1, list2))