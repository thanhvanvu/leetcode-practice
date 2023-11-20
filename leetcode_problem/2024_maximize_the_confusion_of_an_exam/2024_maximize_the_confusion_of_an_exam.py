# https://www.youtube.com/watch?v=gqXU1UyA8pk
# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

def maxConsecutiveAnswers(answerKey, k):
    answerCount = {}
    L = 0
    result = float('-inf')

    for R in range(len(answerKey)):
        answer = answerKey[R]
        answerCount[answer] = 1 + answerCount.get(answer, 0)

        # window size
        window = R - L + 1

        # most frequency answer
        mostF = max(answerCount.values())

        # if we replace answer more than k time
        # move window
        while window - mostF > k:
            aLeft = answerKey[L]
            answerCount[aLeft] -= 1

            L += 1

            # update
            # window size
            window = R - L + 1

            # most frequency answer
            mostF = max(answerCount.values())

        result = max(result, window)

    return result



answerKey = "TTFTTFTT"
k = 1

print(maxConsecutiveAnswers(answerKey, k))
