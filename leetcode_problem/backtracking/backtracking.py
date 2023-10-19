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
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(0)
    return root


# Determine if a path exists from the root of the tree to a leaf node.
# It may not contain any 0
# Kiểm tra xem binary tree có path nào không chứa số 0 ?
# Nếu có 1 branch thỏa điều kiện ==> true

def canReachLeaf(root):
    # base case
    if not root or root.val == 0:
        return False

    # reach the end leaf, meaning that path does not contain 0
    # return True
    if not root.left and not root.right:
        return True

    # if pointer does not reach end leaf yet
    # continue to check
    # recursive step, if reach 0 ==> false and check right branch
    if canReachLeaf(root.left) == True:
        return True

    if canReachLeaf(root.right) == True:
        return True

    return False


# Determine if a path exists from the root of the tree to a leaf node.
# It may not contain any 0
# In ra nhánh không có chứa giá trị 0

def pathNotContainZero(root):
    result = []

    def leftPath(root, path):
        # base case
        if not root or root.val == 0:
            return False

        # append value # 0 into array result
        path.append(root.val)

        # reach the end leaf, meaning that path does not contain 0
        # return True
        if not root.left and not root.right:
            return True

        # if pointer does not reach end leaf yet
        # continue to check
        # recursive step, if reach 0 ==> false and check right branch
        if leftPath(root.left, path) == True:
            return True

        if leftPath(root.right, path) == True:
            return True

        # if reach this line
        # meaning we reach the value 0
        # recursive step:
        # leftPath(left) == false
        # leftPath(right) == false
        # pop the last value to go to another branch
        path.pop()

        return False

    leftPath(root, result)

    return result



# Create a sample binary search tree
root = build_sample_tree()

print(inorder_traversal(root))
print(canReachLeaf(root))
print(pathNotContainZero(root))
