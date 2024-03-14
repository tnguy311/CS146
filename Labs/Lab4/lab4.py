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
        
# If the tree is empty, there's nothing to invert then return None
# Then swap the left and right children of the current node
# Recursively invert the left subtree, recursively invert the right subtree
# Return the root of the inverted tree
