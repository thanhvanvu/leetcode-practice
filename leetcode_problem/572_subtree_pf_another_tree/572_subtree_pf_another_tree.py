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
        self.root = TreeNode(3)
        self.root.left = TreeNode(4)
        self.root.right = TreeNode(5)
        self.root.left.left = TreeNode(12)
        self.root.left.right = TreeNode(2)

    def build_sub_tree(self):
        """Build a sample binary search tree."""
        self.root = TreeNode(4)
        self.root.left = TreeNode(1)
        self.root.right = TreeNode(23)

    def isSubtree(self, root, subRoot):
        # base case
        # subroot can also be subtree if subRoot is None
        if subRoot is None:
            return True

        if root is None:
            return False

        if self.isSameTree(root, subRoot) is True:
            return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        # Return True if either the left or right subtree contains subRoot.
        return left or right

    def isSameTree(self, cur, sub):
        if cur is None and sub is None:
            return True
        if cur is None or sub is None:
            return False
        if cur.val != sub.val:
            return False

        left = self.isSameTree(cur.left, sub.left)
        right = self.isSameTree(cur.right, sub.right)

        if left is True and right is True:
            return True
        else:
            return False


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
p = bst.build_sample_tree()

q = bst.build_sub_tree()

# before inverting
print(levelOrder(bst.root))

print(bst.isSubtree(p, q))


# O(n x m)
# n is # of node of root
# m is # of node of subRoot
