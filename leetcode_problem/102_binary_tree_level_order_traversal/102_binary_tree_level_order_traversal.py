# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# https://www.youtube.com/watch?v=6ZnyEApgFYg
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# iterative solution


def levelOrder(root):
    queue = deque()
    result = []
    if root is not None:
        queue.append(root)

    level = 0

    while len(queue) > 0:
        print("level: ", level)

        level_array = []
        for i in range(len(queue)):

            curr = queue.popleft()
            print(curr.val)

            level_array.append(curr.val)

            # should append left -> right to queue
            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        level += 1
        result.append(level_array)

    return result


def levelOrder_practice(root):  # iterative solution
    queue = deque()
    result = []

    if root is not None:
        queue.append(root)

    while len(queue) > 0:
        level_array = []

        for i in range(len(queue)):
            cur = queue.popleft()

            level_array.append(cur.val)

            # check if node has right or left node ?
            if cur.left is not None:
                queue.append(cur.left)

            if cur.right is not None:
                queue.append(cur.right)

        # after for loop is done
        # it means, all nodes at h level are added to stack
        result.append(level_array)

    return result


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

print(levelOrder_practice(root))
