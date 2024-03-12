class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        def validate(node, minVal, maxVal):
            if not node:
                return True
            if not (minVal < node.val < maxVal):
                return False
            return validate(node.left, minVal, node.val) and validate(node.right, node.val, maxVal)
        
        return validate(root, float('-inf'), float('inf'))
