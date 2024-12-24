def findDuplicate(nums) -> int:
    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)


lst = [1,3,4,2,2]
print(findDuplicate(lst))