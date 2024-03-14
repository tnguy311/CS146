class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        if root is None:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        if root.left is not None:
            self.invertTree(root.left)

        if root.right is not None:
            self.invertTree(root.right)

        return root


# If the tree is empty, we return None as there's nothing to invert.
# For each non-None node in the tree, we swap its left and right children. Inverts the subtree rooted at this node.
# After swapping the children, we recursively call the `invertTree` function for both the left and right children of the current node. This repeats the swapping process for each subtree.
# Finally, we return the root node of the inverted tree.
