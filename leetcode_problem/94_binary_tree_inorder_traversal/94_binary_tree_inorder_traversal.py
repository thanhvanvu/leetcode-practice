# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# https://www.youtube.com/watch?v=g_S5WuasWUE

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive way
def inorder_traversal(root):
    result = []

    def traversal(root):
        if root is None:
            return

        traversal(root.left)
        result.append(root.val)
        traversal(root.right)

    traversal(root)

    return result


# iterative solution
def inorder_traversal_iterative(root):
    stack = []
    cur = root
    result = []

    while cur or stack:

        # traversal to the most left node
        # whenever see the node, add to stack
        while cur is not None:
            stack.append(cur)
            cur = cur.left

        # when the left node is None, break while loop
        # pop the node from the stack
        # move pointer cur to that node
        cur = stack.pop()
        result.append(cur.val)

        # traversal to the right
        cur = cur.right

    return result


# Helper function to build a sample binary search tree
def build_sample_tree():
    # Create nodes for a sample BST
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    return root


# Create a sample binary search tree
root = build_sample_tree()

print(inorder_traversal_iterative(root))
