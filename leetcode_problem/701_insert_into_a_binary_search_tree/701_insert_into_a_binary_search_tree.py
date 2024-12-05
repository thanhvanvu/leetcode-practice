# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
# https://www.youtube.com/watch?v=Cpg8f79luEA

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insertIntoBST(self, root, val):
        # case tree is empty
        if root is None:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        return root

    def insert_iterative(self, root, val):
        # case tree is empty
        if root is None:
            return TreeNode(val)

        current = root

        # just loop until the left node
        while True:
            if val > current.val:
                # cant go to right anymore (left node)
                if current.right is None:
                    current.right = TreeNode(val)  # insert new node
                    return root

                # update new node
                current = current.right

            if val < current.val:
                if current.left is None:
                    current.left = TreeNode(val)
                    return root

                current = current.left

    def search(self, root, val):
        """Search for a value in the BST."""
        while root is not None:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root
        return None

    def print_subtree(self, root):
        """Print the subtree in an in-order traversal."""
        if root is not None:
            self.print_subtree(root.left)
            print(root.val, end=' ')
            self.print_subtree(root.right)

    def build_sample_tree(self):
        """Build a sample binary search tree."""
        self.root = TreeNode(4)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(7)
        self.root.left.left = TreeNode(1)
        self.root.left.right = TreeNode(3)


bst = TreeNode()

bst.build_sample_tree()

bst.insertIntoBST(bst.root, 5)

bst.print_subtree(bst.root)
