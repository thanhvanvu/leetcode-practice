def minOperations(s: str):
    count = 0  # operations if s start with 0

    for i in range(len(s)):
        if i % 2:  # odd
            if s[i] == "0":
                count += 1
            else:
                count = 0
        else:  # even
            if s[i] == "1":
                count += 1
            else:
                count = 0
    return min(count, len(s) - count)


s = "0100"
print(minOperations(s))
