# https://leetcode.com/problems/plus-one/description/

def plusOne(digits):
    # loop through from end to front
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0

            # [9,9,9]
            if i == 0:
                # [1, 0, 0, 0]
                digits = [1] + digits
        else:
            # if the number is not 9
            # add 1 and break loop
            digits[i] += 1
            break

    return digits


input = [9, 9]
print(plusOne(input))
