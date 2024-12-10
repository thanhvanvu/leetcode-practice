# https://www.youtube.com/watch?v=LSKQyOz_P8I&t=362s
# https://leetcode.com/problems/path-sum/description/

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
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)

    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)

    root.right.right.right = TreeNode(1)
    return root


def hasPathSum(root, targetSum):
    def dfs(node, curSum):

        # case: empty tree
        if not node:
            return False

        # take value from the node
        # add to curSum
        curSum += node.val

        # if pointer reaches end leaf node
        # no left or right children
        if node.left is None and node.right is None:
            if curSum == targetSum:
                return True
            else:
                return False

        if dfs(node.left, curSum) == True:
            return True

        if  dfs(node.right, curSum) == True:
            return True

    return dfs(root, 0)


def hasPathSum_practice(root, targetSum):
    # because we keep track curSum
    # need helper function

    def dfs(node, curSum):
        if node is None:
            return False

        # calculate sum total
        curSum = curSum + node.val

        # definition of leaf node
        if node.left is None and node.right is None:
            if curSum == targetSum:
                return True
            else:
                return False

        # recursive left, right
        left_sum = dfs(node.left, curSum)
        right_sum = dfs(node.right, curSum)

        # return True if we see either left tree or right tree has path sum == target
        return left_sum or right_sum

    return dfs(root, 0)





# Create a sample binary search tree
root = build_sample_tree()

print(inorder_traversal_iterative(root))
print(hasPathSum_practice(root, 22))
