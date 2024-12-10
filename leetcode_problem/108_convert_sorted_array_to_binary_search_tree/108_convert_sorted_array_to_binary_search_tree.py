# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
# https://www.youtube.com/watch?v=0K0uCMYq5ng

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.balanced = None
        self.val = val
        self.left = left
        self.right = right

    def sortedArrayToBST(self, nums):
        # because we are doing recursive with L and R
        # create helper function

        def helper(L, R):
            # base case
            if L > R:
                return None

            mid = L + (R - L) // 2

            # create tree node from value of mid
            node = TreeNode(nums[mid])

            # recursive left and right to create new node
            node.left = helper(L, mid - 1)
            node.right = helper(mid + 1, R)

            return node

        L = 0
        R = len(nums) - 1

        return helper(L, R)


def levelOrder(root):
    queue = deque()
    result = []
    if root is not None:
        queue.append(root)

    while len(queue) > 0:

        level_array = []
        for i in range(len(queue)):

            curr = queue.popleft()

            level_array.append(curr.val)

            # should append left -> right to queue
            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)
        result.append(level_array)

    return result


bst = TreeNode()

nums = [-10, -3, 0, 5, 9]
print(bst.sortedArrayToBST(nums))
print(levelOrder(bst.sortedArrayToBST(nums)))
