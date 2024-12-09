# https://leetcode.com/problems/diameter-of-binary-tree/description/
# https://neetcode.io/solutions/diameter-of-binary-tree

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

    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        # return height
        def dfs(cur):
            if cur is None:
                return 0

            left_height = dfs(cur.left)
            right_height = dfs(cur.right)

            # formula
            self.diameter = max(self.diameter, left_height + right_height)

            height = 1 + max(left_height, right_height)

            return height

        dfs(root)

        return self.diameter


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

print(bst.diameterOfBinaryTree(bst.root))
