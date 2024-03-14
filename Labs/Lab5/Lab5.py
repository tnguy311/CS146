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



# We define a TreeNode class to represent the nodes of the binary tree, similar to the Java implementation.
# Public method `isValidBST' takes the root of the binary tree as input and returns a boolean whether the tree is a valid BST. 
# At each node, it checks if the node's value is within the valid range defined by `min_val` and `max_val`. If the node's value not in this range, the method returns false, indicating the tree is not a valid BST. Otherwise, it calls itself for the left and right subtrees, updating the `min_val` and `max_val` values.
# If the current node is None indicating the end of a branch, the method returns true.
