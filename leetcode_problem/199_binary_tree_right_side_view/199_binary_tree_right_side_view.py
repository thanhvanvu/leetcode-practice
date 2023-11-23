# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# https://www.youtube.com/watch?v=d4zLyf32e3I
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# iterative solution


def rightSideView(root):
    queue = deque()
    result = []

    if root:
        queue.append(root)

    while len(queue) > 0:
        rightSide = None
        for i in range(len(queue)):
            curr = queue.popleft()

            # assign all node to rightSide
            # when for loop is done
            # rightSide will be a most right node
            if curr:
                rightSide = curr

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        if rightSide:
            result.append(rightSide.val)

    print(result)


# Helper function to build a sample binary search tree
def build_sample_tree():
    # Create nodes for a sample BST
    root = TreeNode(4)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    return root


# Create a sample binary search tree
root = build_sample_tree()

print(rightSideView(root))
