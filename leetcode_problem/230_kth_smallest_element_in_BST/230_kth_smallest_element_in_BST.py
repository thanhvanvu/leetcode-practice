# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# https://www.youtube.com/watch?v=5LUXSvjmGCw

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root, k):
    stack = []
    cur = root
    count = 0

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left

        # notice that whenever pop the node
        # it will be from smallest to largest
        # whenever popping, update count++
        # check if count == k
        # return the value of that node
        cur = stack.pop()
        count += 1
        if count == k:
            return cur.val

        cur = cur.right


# Helper function to build a sample binary search tree
def build_sample_tree():
    # Create nodes for a sample BST
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    return root


# Create a sample binary search tree
root = build_sample_tree()

print(kthSmallest(root, 1))
