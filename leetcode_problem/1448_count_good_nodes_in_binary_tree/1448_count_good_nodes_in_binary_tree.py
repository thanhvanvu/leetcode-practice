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

    def goodNodes(self, root):

        def dfs(cur, maxValue):
            # base case
            if cur is None:
                return 0

            if cur.val >= maxValue:
                res = 1
            else:
                res = 0

            # update max value
            maxValue = max(maxValue, cur.val)

            res = res + dfs(cur.left, maxValue)
            res = res + dfs(cur.right, maxValue)

            return res

        return dfs(root, root.val)



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

print(bst.goodNodes(bst.root))


# O(n x m)
# n is # of node of root
# m is # of node of subRoot
