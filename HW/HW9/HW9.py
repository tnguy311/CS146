class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        currentNode = root
        
        while currentNode:
            if p.val < currentNode.val and q.val < currentNode.val:
                currentNode = currentNode.left
            elif p.val > currentNode.val and q.val > currentNode.val:
                currentNode = currentNode.right
            else:
                return currentNode
        
        return None


# We start with the root of the tree
# Keep searching until we find the solution
# If both p and q are less than the current node, go left
# If both p and q more than the current node, go right
# If neither of the above cases are true, we've found our LCA
