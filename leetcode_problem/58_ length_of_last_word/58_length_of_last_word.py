

def lengthOfLastWord(s):
    # trim front and end space
    stripped = s.strip()
    length = 0
    for i in range(len(stripped) - 1, -1, -1):
        if stripped[i] == ' ':
            break
        length += 1
    return length


def lengthOfLastWord_1(s):
    s = s.split(" ")
    for i in range(len(s) - 1, -1, -1):
        if s[i] != "":
            last_word = s[i]
            return len(last_word)


string = "Hello World"
print(lengthOfLastWord_1(string))
