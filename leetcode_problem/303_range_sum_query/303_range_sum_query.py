# https://leetcode.com/problems/range-sum-query-immutable/
# https://www.youtube.com/watch?v=2pndAmo_sMA
class NumArray:

    def __init__(self, nums):
        self.prefix = []
        self.L = 0
        self.R = 0

        total = 0

        for n in nums:
            total = total + n
            self.prefix.append(total)

        print(self.prefix)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            self.L = 0
        else:
            self.L = self.prefix[left - 1]
        self.R = self.prefix[right]

        return self.R - self.L


# Your NumArray object will be instantiated and called as such:
lst = [-2, 0, 3, -5, 2, -1]
obj = NumArray(lst)
print(obj.sumRange(0, 2))
print(obj.sumRange(0,5))
