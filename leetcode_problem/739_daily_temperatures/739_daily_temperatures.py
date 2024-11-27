def dailyTemperatures(temperatures):
    output = [0] * len(temperatures)

    stack = []  # pair: [temp, index]

    for i, t in enumerate(temperatures):

        # if current temp is smaller than temp in stack
        # break while loop
        while stack and t > stack[-1][0]:
            stackTemp, stackIndex = stack.pop()  # this step looks like i-=1

            # update the different value for the temperature we just pop
            output[stackIndex] = i - stackIndex

        # if we see the temp in stack > current temp
        # append current temp to stack
        stack.append([t, i])

    return output

def dailyTemperatures_practice(temperatures):
    output = [0] * len(temperatures)

    stack = [] # pair: [index, temp]

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][1]:
            index, temp = stack.pop()
            diff = i - index

            # set value
            output[index] = diff

        stack.append([i, t])
    return output

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures_practice(temperatures))
