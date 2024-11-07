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


def topKFrequent_practice(nums, k):
    # [[], [], [], [], [], []]
    freq = [[] for i in range(len(nums) + 1)]

    # count number
    count = {}

    output = []

    for i in nums:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    # bucket sort
    for element in count:
        key = element
        val = count[element]

        freq[val].append(key)

    print(freq)
    # [[], [3], [2], [1], [], []]
    # it means: 1 occurs 3 times, 2 occurs 2 times, 3 occurs 1 time
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            output.append(n)

            # check if result has k most frequent elements.
            if len(output) == k:
                return output


list_nums = [1,1,1,2,2,2,3]
value = 2

print(topKFrequent_practice(list_nums, value))
