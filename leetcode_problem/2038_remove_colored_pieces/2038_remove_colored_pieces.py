def winnerOfGame(colors):
    alice = 0
    bob = 0

    for i in range(1, len(colors) - 1):
        print(colors[i - 1], colors[i], colors[i + 1])
        if colors[i] == "A" and colors[i] == colors[i - 1] and colors[i] == colors[i + 1]:
            alice += 1
        elif colors[i] == "B" and colors[i] == colors[i - 1] and colors[i] == colors[i + 1]:
            bob += 1

    return True if alice > bob else False


colors = "ABBBBBBBAAA"
print(winnerOfGame(colors))
