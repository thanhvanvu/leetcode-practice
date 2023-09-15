# https://leetcode.com/problems/top-k-frequent-elements/
# https://www.youtube.com/watch?v=YPTqKIgVk-k

def topKFrequent(nums, k):
    countNum = {}
    result = []
    freq = [[] for i in range(len(nums) + 1)]  # [[], [], [], [], [], []]

    # code to count the number and put in the hashmap
    # dict_items([(1, 3), (2, 2), (3, 1)])
    # (1,3): the number 1 occurs 3 times
    for i in nums:
        if i not in countNum:
            countNum[i] = 1
        else:
            countNum[i] += 1

    # use bucket sort technique
    # [[], [3], [2], [1], [], [], []]
    # index 3: number 1 occurs 3 times
    # index 2: number 2 occurs 2 times
    for number, count in countNum.items():
        freq[count].append(number)

    # reverse loop
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            result.append(n)

            # check if result has k most frequent elements.
            if len(result) == k:
                return result


list_nums = [1, 1, 1, 2, 2, 3]
value = 2

print(topKFrequent(list_nums, value))
