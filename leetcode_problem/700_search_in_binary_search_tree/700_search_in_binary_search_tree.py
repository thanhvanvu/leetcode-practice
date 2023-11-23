class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_subtree(root):
    if root is not None:
        print_subtree(root.left)
        print(root.val, end=' ')
        print_subtree(root.right)


# Helper function to build a sample binary search tree
def build_sample_tree():
    # Create nodes for a sample BST
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    return root


def searchBST(root, val: int):
    # if root reaches to leaf node (root == None)
    # while loop will stop
    while root is not None:
        if val < root.val:
            root = root.left
        elif val > root.val:
            root = root.right
        else:
            return root


# Create a sample binary search tree
root = build_sample_tree()

print(print_subtree(searchBST(root, 2)))
