# https://leetcode.com/problems/invert-binary-tree/description/
# https://www.youtube.com/watch?v=OnSn2XEQ4MY
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
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

    def invertTree(self, root):
        if root is None:
            return None

        # swap the children
        root.left, root.right = root.right, root.left

        # go left
        self.invertTree(root.left)

        # go right
        self.invertTree(root.right)

        return root


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

bst.invertTree(bst.root)

# after inverting
print(levelOrder(bst.root))
