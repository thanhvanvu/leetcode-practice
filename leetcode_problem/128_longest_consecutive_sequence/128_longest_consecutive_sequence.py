# https://leetcode.com/problems/longest-consecutive-sequence/description/
# https://www.youtube.com/watch?v=P6RZZMu_maU

def longestConsecutive(nums):
    hashSet = set(nums)  # {100, 4, 200, 1, 3, 2}
    longest = 0
    for i in nums:
        # check if left neighbor is in hashSet
        # if not ==> sequence start
        # 100: 99 is not in hashSet ==> start 100:...
        if i - 1 not in hashSet:
            count = 1

            # check if 101, 102, 103...is in hashSet ?
            # if yes, count + 1
            while i + count in hashSet:
                count += 1

            longest = max(longest, count)

    return longest


nums = [100, 4, 200, 1, 3, 2]

print(longestConsecutive(nums))
