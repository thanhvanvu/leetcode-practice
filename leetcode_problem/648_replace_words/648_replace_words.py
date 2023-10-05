def replaceWords(dictionary, sentence):
    dicSet = set(dictionary)

    sentence = sentence.split()

    for i in range(len(sentence)):
        word = sentence[i]
        subString = ''
        for j in range(len(word)):
            subString = subString + word[j]
            if subString in dicSet:
                sentence[i] = subString
                break

    return " ".join(sentence)


def replaceWords2(dictionary, sentence):
    dictionary = sorted(dictionary)  # ['bat', 'cat', 'catt', 'rat']
    sentence = sentence.split()  # ['the', 'cattle', 'was', 'rattled', 'by', 'the', 'battery']

    # loop through sentence
    for item in range(len(sentence)):
        for word in dictionary:
            # check if item in sentence starts with item in dict?
            # yes ==> replace
            if sentence[item].startswith(word):
                sentence[item] = word

    return " ".join(sentence)


dictionary = ["catt", "cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"

print(replaceWords2(dictionary, sentence))
