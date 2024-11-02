# https://leetcode.com/problems/number-of-good-pairs/description/
# https://www.youtube.com/watch?v=BqhDFUo1rjs

# using 2 for loop
def numIdenticalPairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count += 1

    return count


# using math
def numIdenticalPairs_2(nums):
    hashCount = {}

    for i in nums:
        if i not in hashCount:
            hashCount[i] = 1
        else:
            hashCount[i] += 1

    # math
    # [count * (count - 1 )] /2

    result = 0
    for i in hashCount:
        value = hashCount[i]
        result += int((value * (value - 1)) / 2)

    return result


nums = [1, 2, 3, 1, 1, 3]

print(numIdenticalPairs_2(nums))
