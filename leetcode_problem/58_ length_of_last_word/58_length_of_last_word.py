def lengthOfLastWord(s):
    # trim front and end space
    stripped = s.strip()
    length = 0
    for i in range(len(stripped) - 1, -1, -1):
        if stripped[i] == ' ':
            break
        length += 1
    return length


string = "aa"
print(lengthOfLastWord(string))
