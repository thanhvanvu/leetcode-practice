# https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=j4KwhBziOpg

import random


class RandomizedSet(object):

    def __init__(self):
        self.hashNums = {}
        self.arrayNums = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val not in self.hashNums:
            # index will be the last index in array
            self.hashNums[val] = len(self.arrayNums)
            self.arrayNums.append(val)
            return True
        else:
            return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hashNums:
            # get index of the val form hashNums
            index = self.hashNums[val]
            lastNum = self.arrayNums[-1]

            # overwrite the val we want to remove with last num
            # [1, 2, 3, 4, 5]
            # remove 3
            # [1, 2, 5, 4, 5]
            # pop last index ==>
            # [1, 2, 5, 4]
            self.arrayNums[index] = lastNum

            # delete value from arrayNums
            self.arrayNums.pop()

            # update the last num with new index
            # new index is the index of the value we want to pop
            # {1:0, 2:1, 3:2, 4:3, 5:4}
            # remove 3
            # use index of value 3 for last value (5)
            # {1:0, 2:1, 3:2, 4:3, 5:2}
            # remove given value from hashTable
            # {1:0, 2:1, 4:3, 5:2}

            self.hashNums[lastNum] = index
            # delete value from hashNums
            self.hashNums.pop(val)

            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        res = random.choice(self.arrayNums)
        return res

    def print(self):
        print(self.arrayNums)
        print(self.hashNums)


# to getRandom, we need to use array

# to remove the value from the array with O(1)
# we need to use hashMap to check the index of the value
# when inserting the new value to array
# insert key: value to hashMap with key = number, value = index
# 2: 5 ==> number 2 is at index 5 in the array


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
obj.insert(1)
obj.insert(2)
obj.insert(5)
obj.insert(10)
obj.insert(6)

obj.remove(5)
obj.remove(10)
print(obj.getRandom())
obj.print()
# obj.remove(val)
