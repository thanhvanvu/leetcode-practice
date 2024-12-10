# https://leetcode.com/problems/merge-two-binary-trees/description/
# https://www.youtube.com/watch?v=QHH6rIK3dDQ

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

    def mergeTrees(self, root1, root2):
        # base case
        if root1 is None and root2 is None:
            return None

        if root1 is None:
            v1 = 0
        else:
            v1 = root1.val

        if root2 is None:
            v2 = 0
        else:
            v2 = root2.val

        val = v1 + v2

        # create a new node
        node = TreeNode(val)

        # root1 left, root2 left could possibly be None
        node.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        node.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        return node




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

print(bst.mergeTrees(p, q))


# O(n x m)
# n is # of node of root
# m is # of node of subRoot
