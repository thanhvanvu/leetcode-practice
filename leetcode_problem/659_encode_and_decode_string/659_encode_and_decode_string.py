def encode(strs):
    result = ""
    for string in strs:
        result += str(len(string)) + "#" + string

    return result


def decode(str):
    result = []
    i = 0

    print(str)

    while i < len(str):
        j = i

        # loop through until we see #
        # 12#lint
        # j will increase until we see #
        # => j = 1
        # length = [i, j]
        while str[j] != "#":
            j += 1

        length = int(str[i:j])
        rangeString = length + j + 1
        string = str[j + 1: rangeString]

        result.append(string)

        i = rangeString
    return result


input = ["lint", "code", "love", "you"]

print(encode(input))
print(decode(encode(input)))
