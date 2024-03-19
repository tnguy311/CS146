import java.util.*;

public class BinaryTreeTraversal {
   
    static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {}

        TreeNode(int val) { this.val = val; }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    
    
    static class Solution {
        public List<List<Integer>> levelOrder(TreeNode root) {
            List<List<Integer>> result = new ArrayList<>();
            if (root == null)
                return result;

            Queue<TreeNode> queue = new LinkedList<>();
            queue.add(root);

            while (!queue.isEmpty()) {
                int size = queue.size();
                List<Integer> levelNodes = new ArrayList<>();
                for (int i = 0; i < size; i++) {
                    TreeNode current = queue.poll();
                    levelNodes.add(current.val);
                    if (current.left != null)
                        queue.add(current.left);
                    if (current.right != null)
                        queue.add(current.right);
                }
                result.add(levelNodes);
            }
            return result;
        }
    }

    
    public static void main(String[] args) {
        // Example usage
        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(3);
        root.right = new TreeNode(8);
        root.left.left = new TreeNode(1);
        root.right.left = new TreeNode(5);
        root.right.right = new TreeNode(9);

        Solution solution = new Solution();
        List<List<Integer>> traversalResult = solution.levelOrder(root);
        System.out.println(traversalResult);  
    }
}

// Define TreeNode class: The TreeNode class represents a node in a binary tree. It contains attributes for the node value, left child, and right child. Constructors are provided for initializing the node with or without child nodes.

// Define Solution class: The Solution class contains the levelOrder method, which performs a level-order traversal of a binary tree. It uses a queue-based approach to traverse the tree level by level, storing the values of nodes at each level in a list of lists.

// Main method (for testing): The main method serves as a testing ground for the BinaryTreeTraversal class. It creates an example binary tree, invokes the levelOrder method to perform the traversal, and prints the resulting level-order traversal to the console.

// Output: [[4], [3, 8], [1, 5, 9]]: This line indicates the expected output of the level-order traversal performed in the main method. Each inner list represents the values of nodes at a particular level of the binary tree.

