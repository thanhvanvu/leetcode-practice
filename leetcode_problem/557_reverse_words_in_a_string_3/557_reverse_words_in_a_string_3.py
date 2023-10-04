def reverseWords(s):
    l = 0
    r = 0

    # convert string to array, so i can swap char
    s_list = list(s)

    # loop through the list
    for i in range(len(s_list)):
        # if see space ' '
        # or pointer reach the end
        # set r pointer to the last character before space ' '
        if s_list[i] == ' ' or i == len(s_list) - 1:

            # if i reach the end
            # r = i
            if i == len(s_list) - 1:
                r = i
            else:
                r = i - 1

            # swap character
            while l < r:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1

            # update l to the first char of the next word
            l = i + 1

    return "".join(s_list)


s = "Let's take LeetCode contest"
print(reverseWords(s))
