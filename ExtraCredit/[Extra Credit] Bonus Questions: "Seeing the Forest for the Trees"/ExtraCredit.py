class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Balance the tree if necessary
        if balance > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        elif balance < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        
        return root
    
    def delete(self, root, key):
        if not root:
            return root
        
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left or not root.right:
                if root.left:
                    temp = root.left
                else:
                    temp = root.right
                
                if not temp:
                    temp = root
                    root = None
                else:
                    root = temp
                
                del temp
            else:
                temp = self.get_min_value_node(root.right)
                root.key = temp.key
                root.right = self.delete(root.right, temp.key)
            
        if not root:
            return root
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Rebalance the tree if necessary
        if balance > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        elif balance < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        
        return root
    
    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=" ")
            self.inorder_traversal(root.right)
    
    def get_height(self, root):
        if not root:
            return 0
        return root.height
    
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    
    def get_min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current
    
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
    
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x


#This Python code defines an AVL tree
#The TreeNode class represents each node in the tree, storing a key values and a height attribute. 
#The AVLTree class contains methods for insertion, deletion, and inorder traversal. 
#Insert method adds new nodes maintaining balance by adjusting heights and performing rotations.
#Deletion removes nodes, handling various cases of node removal and adjusting heights. 
#The inorder_traversal method prints node keys in sorted order by traversing left, visiting the current nod then traversing right. 
#Utility methods get_height, get_balance and get_min_value_node calculate heights, balance factors, and find minimum value node. 
#Rotation operations, left_rotate and right_rotate, balanced the tree structure during insertions and deletions.
