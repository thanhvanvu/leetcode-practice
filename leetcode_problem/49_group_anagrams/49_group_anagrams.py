from collections import defaultdict


# O(m.n.26)
def groupAnagrams(strs):
    # hashmap
    result = defaultdict(list)  # mapping charCount to list of Anagrams

    for s in strs:
        # for every string, create count
        count = [0] * 26

        # for every char, map char to index
        # a => 0, b => 1, c => 2
        # ord(c) - ord("a")
        for char in s:
            index = ord(char) - ord("a")
            count[index] += 1

        # key: [1, 0, 0, 0, 1, 0, 0]
        # if we see the same key, append that string to hashmap
        result[tuple(count)].append(s)

    return result.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
