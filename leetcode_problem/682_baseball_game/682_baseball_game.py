# https://www.youtube.com/watch?v=Id_tqGdsZQI
# https://leetcode.com/problems/baseball-game/

def calPoints(operations):
    record = []

    for op in operations:
        if op == 'C':
            record.pop()
        elif op == 'D':
            newScore = 2 * record[-1]
            record.append(newScore)
        elif op == '+':
            newScore = record[-1] + record[-2]
            record.append(newScore)
        else:
            record.append(int(op))

    total = sum(record)

    return total


def calPoints_practice(operations):
    stack = []
    for op in operations:
        if op == "C":
            stack.pop()
        elif op == "D":
            a = stack[-1]
            result = 2 * int(a)
            stack.append(result)
        elif op == "+":
            a = stack[-1]
            b = stack[-2]
            result = int(a) + int(b)
            stack.append(result)
        else:
            stack.append(op)

    score = 0
    for num in stack:
        score += int(num)

    return score


if __name__ == '__main__':
    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    length_arr = len(ops)

    a = calPoints_practice(ops)

    print('Total', a)
