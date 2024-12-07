# https://leetcode.com/problems/balanced-binary-tree/description/
# https://www.youtube.com/watch?v=QfJsau0ItOY

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.balanced = None
        self.val = val
        self.left = left
        self.right = right

    def build_sample_tree(self):
        """Build a sample binary search tree."""
        self.root = TreeNode(4)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(7)
        self.root.left.left = TreeNode(1)
        self.root.left.right = TreeNode(3)

    # to be able to solve isBalanced
    # solve this below problem first using recursive
    # maximum-depth-of-binary-tree
    def isBalanced(self, root):
        self.balanced = True

        def dfs(root):
            # base case root is None
            # return 0 -> 0 is height
            if root is None:
                return 0

            # traversal left and right node
            left_height = dfs(root.left)
            right_height = dfs(root.right)

            # calculate different btw left height node and right height node
            diff = abs(left_height - right_height)

            if diff > 1:
                self.balanced = False

            return 1 + max(left_height, right_height)

        dfs(root)

        return self.balanced


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

# idea is
# go from bottom to top
# go to leaf node -> check if that node is balanced ?
# to check balanced, calculate the height of left and right node
# heightLeft - heightRight <= 1 => balanced
print(bst.isBalanced(bst.root))
