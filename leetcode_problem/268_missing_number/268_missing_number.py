def missingNumber(nums):
    setNum = set()

    for i in range(0,len(nums) +1):
        setNum.add(i)

    for num in nums:
        if num in setNum:
            setNum.discard(num)

    return setNum.pop()


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missingNumber(nums))