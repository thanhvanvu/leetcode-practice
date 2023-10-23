# https://leetcode.com/problems/relative-ranks/description/

import heapq


def findRelativeRanks_myself(score):
    # convert positive to negative array
    score_heap = [-i for i in score]

    # transform list to heap
    heapq.heapify(score_heap)

    k = 0

    while k < len(score):
        # get maximum score
        maximum = abs(heapq.heappop(score_heap))

        # find index of the score in list
        place = score.index(maximum)

        # replace value with string
        if k == 0:
            score[place] = "Gold Medal"
        elif k == 1:
            score[place] = "Silver Medal"
        elif k == 2:
            score[place] = "Bronze Medal"
        else:
            score[place] = str(k + 1)

        k += 1

    return score


def findRelativeRanks(score):
    # sort the array in descending order
    sorted_scores = sorted(score, reverse=True)

    # create hash table
    hash_rank = {}

    # store score and rank to hash table
    # {5: 'Gold Medal', 4: 'Silver Medal', 3: 'Bronze Medal', 2: '4', 1: '5'}
    for i in range(len(sorted_scores)):
        if i == 0:
            hash_rank[sorted_scores[i]] = "Gold Medal"
        elif i == 1:
            hash_rank[sorted_scores[i]] = "Silver Medal"
        elif i == 2:
            hash_rank[sorted_scores[i]] = "Bronze Medal"
        else:
            hash_rank[sorted_scores[i]] = str(i + 1)

    # loop through score array
    # replace score with rank
    for i in range(len(score)):
        score_value = score[i]
        score[i] = hash_rank[score_value]

    return score


score = [5, 4, 3, 2, 1]
print(findRelativeRanks(score))
