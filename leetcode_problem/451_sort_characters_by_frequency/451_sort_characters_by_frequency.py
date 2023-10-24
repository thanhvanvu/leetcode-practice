# https://leetcode.com/problems/sort-characters-by-frequency/description/

def frequencySort(s):
    hashChar = {}
    string = ""

    for i in s:
        if i not in hashChar:
            hashChar[i] = 1
        else:
            hashChar[i] += 1

    # dict_items([('A', 1), ('a', 1), ('b', 2)])
    # sort it in descending order.
    sorted_chars = sorted(hashChar.items(), key=lambda letter: (letter[1]), reverse=True)

    for char, num in sorted_chars:
        # s * 2 ==> ss
        # k * 3 ==> kkk
        string += char * num

    return string


s = "Aabb"
print(frequencySort(s))
