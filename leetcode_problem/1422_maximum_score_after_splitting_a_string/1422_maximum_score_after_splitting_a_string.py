# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/
# https://www.youtube.com/watch?v=mc_eSStDrWw

def maxScore(s: str):
    zero = 0
    one = s.count("1")
    maxOutput = float("-inf")

    # len(s) - 1: do not want to add the last element to left substring
    for i in range(len(s) - 1):
        if s[i] == "0":
            zero += 1
        else:
            one -= 1

        maxOutput = max(maxOutput, zero + one)

    return maxOutput

# s = "011101"
# count # of 1
# loop through s
# if we see 0, zero + 1
# if we see 1, one - 1
# calculate score = zero + one
# assign maxOutput


s = "011101"
print(maxScore(s))
