# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
# https://www.youtube.com/watch?v=gs2LMfuOR9k

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.balanced = None
        self.val = val
        self.left = left
        self.right = right

    def build_sample_tree(self):
        """Build a sample binary search tree."""
        self.root = TreeNode(6)

        self.root.left = TreeNode(2)
        self.root.right = TreeNode(8)

        self.root.left.left = TreeNode(0)
        self.root.left.right = TreeNode(4)

        self.root.left.right.left = TreeNode(3)
        self.root.left.right.right = TreeNode(5)

        self.root.right.left = TreeNode(7)
        self.root.right.right = TreeNode(9)

    def build_sub_tree(self):
        """Build a sample binary search tree."""
        self.root = TreeNode(4)
        self.root.left = TreeNode(1)
        self.root.right = TreeNode(23)

    def lowestCommonAncestor(self, root, p, q):
        cur = root

        # guarantee the result
        # just use while
        while cur is not None:
            # case 2 val of p, q > cur.val
            # we go to right tree
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right

            # case 2 val of p, q < cur.val
            # we go to left tree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left

            # case 2 val of p.val <= cur.val <= q.val or q.val < cur.val < p.val
            # - p and q are on different sides of cur
            # - One of p or q is equal to cur
            # it means we see the split occurs
            # we return cur
            elif (p.val <= cur.val <= q.val) or (q.val <= cur.val <= p.val):
                return cur


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
p = bst.root.right.left
q = bst.root.right.right

# before inverting
print(levelOrder(bst.root))

print(bst.lowestCommonAncestor(bst.root, p, q).val)


# O(n x m)
# n is # of node of root
# m is # of node of subRoot
