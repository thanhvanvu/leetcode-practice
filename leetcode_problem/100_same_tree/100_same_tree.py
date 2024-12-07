# https://leetcode.com/problems/same-tree/description/
# https://www.youtube.com/watch?v=vRbbcKXCxOw

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.balanced = None
        self.val = val
        self.left = left
        self.right = right

    def build_sample_tree_1(self):
        """Build a sample binary search tree."""
        self.root = TreeNode(1)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(3)
        self.root.left.left = TreeNode(1)
        self.root.left.right = TreeNode(3)

    def build_sample_tree_2(self):
        """Build a sample binary search tree."""
        self.root = TreeNode(1)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(3)
        self.root.left.left = TreeNode(1)
        self.root.left.right = TreeNode(33)

    def isSameTree(self, p , q):
        # base case

        # both tree are empty
        # => same tree
        if p is None and q is None:
            return True

        # 1 of 2 tree is empty
        # p empty, q = 1
        # p = 1, q empty
        # => not same tree
        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        left_equal = self.isSameTree(p.left, q.left)
        right_equal = self.isSameTree(p.right, q.right)

        if left_equal is True and right_equal is True:
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
q= bst.build_sample_tree_1()
p =bst.build_sample_tree_2()


# idea is
# go from bottom to top
# go to leaf node -> check if that node is balanced ?
# to check balanced, calculate the height of left and right node
# heightLeft - heightRight <= 1 => balanced
print(bst.isSameTree(p, q))
