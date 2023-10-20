# https://www.youtube.com/watch?v=REOH22Xwdkk
# 

def subsets(nums):
    output = []

    subset = []

    # [1, 2, 3] => len = 3
    # i = index

    def dfs(i):
        # base case
        # i >= len => add [subset] into [output]

        # need to make a copy of [subset] then add to [output]
        # otherwise it will modify the [subset]
        if i >= len(nums):
            output.append(subset.copy())
            return

        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)

        # decision not to include nums[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)

    return output

nums = [1, 2, 3]

print(subsets(nums))
