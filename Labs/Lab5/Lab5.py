class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        prev_node = None
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            
            if prev_node is not None and root.val <= prev_node.val:
                return False
            
            prev_node = root
            
            root = root.right
        
        return True

# Initialize variables for in-order traversal
# Perform in-order traversal
# Check if current node violates BST property
# Update previous node
