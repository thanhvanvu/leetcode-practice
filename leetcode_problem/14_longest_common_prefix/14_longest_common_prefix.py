# https://leetcode.com/problems/longest-common-prefix/description/
# https://www.youtube.com/watch?v=0sWShKIJoo4

def longestCommonPrefix_1(strs):
    #  assumption all words have the same length

    prefix = ''

    # get the length of the first word

    for i in range(len(strs[0])):
        # loop through every word
        for word in strs:
            # could be out of bound because
            # ['ab', 'a']
            # i == len(word): make sure it is inbound
            if i == len(word) or word[i] != strs[0][i]:
                return prefix

        prefix += strs[0][i]

    return prefix


def longestCommonPrefix(strs):
    string = strs[0]
    result = ""
    for i in range(len(string)):
        for word in strs:
            if i == len(word) or word[i] != strs[0][i]:
                return result

        result += strs[0][i]

    return result


strings = ["flower", "flow", "flight"]

print(longestCommonPrefix(strings))
