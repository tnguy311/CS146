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
