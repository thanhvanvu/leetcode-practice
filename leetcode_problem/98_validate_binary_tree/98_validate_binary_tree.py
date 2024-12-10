# https://leetcode.com/problems/subtree-of-another-tree/description/
# https://www.youtube.com/watch?v=E36O5SWp-LE&t=835s

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.balanced = None
        self.val = val
        self.left = left
        self.right = right

    def build_sample_tree(self):
        """Build a sample binary search tree."""
        self.root = TreeNode(5)
        self.root.left = TreeNode(3)
        self.root.right = TreeNode(7)
        self.root.right.left = TreeNode(4)
        self.root.right.right = TreeNode(8)


    def isValidBST(self, root):
        # because we need recursive with parameter low, high
        # need to create the helper function

        def validate(root, low, high):
            # base case
            if root is None:
                return True

            # root node must be between low and high
            # else -> keep doing recursive
            if not(low < root.val < high):
                return False

            # recursive step
            left_validate = validate(root.left, low, root.val)
            right_validate = validate(root.right, root.val, high)

            if left_validate is True and right_validate is True:
                return True
            else:
                return False

        return validate(root, float('-inf'), float('inf'))



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
bst.build_sample_tree()
# before inverting
print(levelOrder(bst.root))
print(bst.isValidBST(bst.root))


