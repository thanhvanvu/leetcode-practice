def romanToInt1(s):
    symbol = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    output = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s):
            if s[i] + s[i + 1] in symbol:
                output += symbol[s[i] + s[i + 1]]
                i += 2
            else:
                output += symbol[s[i]]
                i += 1
        else:
            output += symbol[s[i]]
            i += 1

    return output





def romanToInt(s):
    symbol = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    result = 0
    i = 0
    for i in range(len(s)):
        if i + 1 < len(s):
            if symbol[s[i]] < symbol[s[i + 1]]:
                result -= symbol[s[i]]
            else:
                result += symbol[s[i]]
        else:
            result += symbol[s[i]]

    return result

string = "LVIII"
print(romanToInt(string))
