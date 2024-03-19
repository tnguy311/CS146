class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    result = []
    if not root:
        return result
    
    queue = [root]
    
    while queue:
        level_nodes = []
        size = len(queue)
        for _ in range(size):
            current = queue.pop(0)
            level_nodes.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        result.append(level_nodes)
    
    return result

# The TreeNode class defines a node in a binary tree. It provides constructors to create a node with or without child nodes.
# The Solution class contains the levelOrder method, which traverses a binary tree level by level. Using a queue, it stores the values of nodes at each level in a list of lists.
# The main method is used for testing the BinaryTreeTraversal class in Python. It creates an example binary tree, performs the level-order traversal using the levelOrder method, and displays the result.
# The output [[4], [3, 8], [1, 5, 9]] shows the values of nodes at each level of the binary tree obtained from the level-order traversal. Each inner list represents the values at a specific level.
